#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import mimetypes
import os
import re
import smtplib
import subprocess
import sys
import time
import uuid
from email.message import EmailMessage
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Send a local HTML report email with inline local images."
    )
    parser.add_argument("--html-file", required=True, help="Path to local HTML report")
    parser.add_argument("--subject", required=True, help="Email subject")
    parser.add_argument(
        "--to",
        action="append",
        default=[],
        help="Recipient email address, repeatable. Falls back to EMAIL_TO_ADDRS or nt_cam_pulse config.",
    )
    parser.add_argument("--from-addr", help="Override sender address")
    parser.add_argument("--smtp-host", help="Override SMTP host")
    parser.add_argument("--smtp-port", type=int, help="Override SMTP port")
    parser.add_argument("--smtp-username", help="Override SMTP username")
    parser.add_argument("--smtp-password", help="Override SMTP password")
    parser.add_argument(
        "--use-ssl",
        action="store_true",
        help="Use SMTP SSL instead of STARTTLS",
    )
    parser.add_argument(
        "--no-tls",
        action="store_true",
        help="Disable STARTTLS when not using SMTP SSL",
    )
    parser.add_argument(
        "--plain-text",
        help="Optional plain text body. Defaults to a short generated summary.",
    )
    parser.add_argument(
        "--summary",
        help="Optional short summary shown in the email body above attachment notes.",
    )
    parser.add_argument(
        "--attach-file",
        action="append",
        default=[],
        help="Attach an existing local file, repeatable.",
    )
    parser.add_argument(
        "--export-pdf",
        action="store_true",
        help="Export the HTML into a PDF and attach it.",
    )
    parser.add_argument(
        "--export-html-attachment",
        action="store_true",
        help="Export a cleaned HTML attachment and attach it.",
    )
    parser.add_argument(
        "--html-attachment-output",
        help="Optional cleaned HTML attachment path. Defaults to *_email.html.",
    )
    parser.add_argument(
        "--pdf-output",
        help="Optional PDF output path. Defaults to HTML filename with .pdf suffix.",
    )
    parser.add_argument(
        "--chrome-path",
        help="Override Chrome binary path for PDF export.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Build email and validate config, but do not send",
    )
    return parser.parse_args()


def load_env_defaults() -> dict[str, str]:
    env = dict(os.environ)
    candidates = [
        Path.cwd() / ".env",
        Path(__file__).resolve().parents[1] / ".env",
        Path(__file__).resolve().parents[2] / "nt_cam_pulse" / ".env",
        Path("/Users/travis.zhao/nt_cam_pulse/.env"),
    ]
    for path in candidates:
        if not path.exists():
            continue
        for raw_line in path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip("'").strip('"')
            env.setdefault(key, value)
    return env


def resolve_recipients(cli_values: list[str], env: dict[str, str]) -> list[str]:
    if cli_values:
        return [item.strip() for item in cli_values if item.strip()]
    raw = env.get("EMAIL_TO_ADDRS", "").strip()
    if raw:
        normalized = raw.replace(";", ",")
        return [item.strip() for item in normalized.split(",") if item.strip()]
    fallback = env.get("EMAIL_FROM_ADDR", "").strip() or env.get("EMAIL_SMTP_USERNAME", "").strip()
    return [fallback] if fallback else []


def build_plain_text(subject: str, html_path: Path, summary: str | None, attachments: list[Path]) -> str:
    lines = [subject, ""]
    if summary:
        lines.extend([summary, ""])
    lines.append("完整看板请见附件。")
    lines.append(f"源文件: {html_path.resolve()}")
    if attachments:
        lines.append("")
        lines.append("附件:")
        lines.extend(f"- {path.name}" for path in attachments)
    return "\n".join(lines) + "\n"


def build_html_summary(subject: str, summary: str | None, attachments: list[Path]) -> str:
    summary_html = ""
    if summary:
        summary_html = f"<p>{html.escape(summary)}</p>"
    attachment_html = ""
    if attachments:
        items = "".join(f"<li>{html.escape(path.name)}</li>" for path in attachments)
        attachment_html = f"<p><strong>附件</strong></p><ul>{items}</ul>"
    return (
        "<!doctype html><html><body style=\"font-family:Helvetica Neue,PingFang SC,Noto Sans SC,sans-serif;\">"
        f"<h2 style=\"margin:0 0 12px;\">{html.escape(subject)}</h2>"
        f"{summary_html}"
        "<p>完整看板请见附件。</p>"
        f"{attachment_html}"
        "</body></html>"
    )


def build_auto_summary(html_text: str) -> str:
    def extract(label: str) -> str:
        pattern = rf'<div class="label">{re.escape(label)}</div>\s*<div class="value">([^<]+)</div>'
        match = re.search(pattern, html_text)
        return match.group(1).strip() if match else "未知"

    photos = extract("照片事件数")
    users = extract("拍摄用户数")
    ppu = extract("人均拍照张数")
    preset = extract("Preset 用户渗透")
    conclusions = re.findall(r'<div class="callout(?: green)?">(.*?)</div>', html_text, flags=re.DOTALL)
    clean_points = []
    for item in conclusions[:3]:
        text = re.sub(r"<[^>]+>", "", item)
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            clean_points.append(f"- {text}")
    lines = [
        f"本周样本共有 {photos} 照片事件，覆盖 {users} 位拍摄用户，人均拍照张数 {ppu}。",
        f"Preset 用户渗透为 {preset}。",
    ]
    if clean_points:
        lines.append("")
        lines.append("重点结论:")
        lines.extend(clean_points)
    return "\n".join(lines)


def inline_local_images(html_text: str, html_path: Path) -> tuple[str, list[tuple[str, bytes, str, str]]]:
    attachments: list[tuple[str, bytes, str, str]] = []
    seen: dict[Path, str] = {}
    html_dir = html_path.parent
    pattern = re.compile(r'(<img\b[^>]*\bsrc=["\'])([^"\']+)(["\'][^>]*>)', re.IGNORECASE)

    def replace(match: re.Match[str]) -> str:
        prefix, src, suffix = match.groups()
        if re.match(r"^(https?:|cid:|data:|mailto:)", src, re.IGNORECASE):
            return match.group(0)
        candidate = (html_dir / src).resolve()
        if not candidate.exists() or not candidate.is_file():
            return match.group(0)
        if candidate not in seen:
            cid = f"{uuid.uuid4().hex}@imageproduct"
            seen[candidate] = cid
            mime_type, _ = mimetypes.guess_type(candidate.name)
            mime_type = mime_type or "application/octet-stream"
            attachments.append((cid, candidate.read_bytes(), mime_type, candidate.name))
        return f"{prefix}cid:{seen[candidate]}{suffix}"

    return pattern.sub(replace, html_text), attachments


def resolve_chrome_path(override: str | None) -> str:
    candidates = [
        override,
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return candidate
    raise FileNotFoundError("chrome_binary_not_found")


def export_pdf_from_html(html_path: Path, pdf_path: Path, chrome_path: str) -> Path:
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    command = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--allow-file-access-from-files",
        f"--print-to-pdf={str(pdf_path)}",
        html_path.as_uri(),
    ]
    result = subprocess.run(command, capture_output=True, text=True, timeout=120)
    if result.returncode != 0 or not pdf_path.exists():
        raise RuntimeError(
            f"pdf_export_failed: code={result.returncode}, stderr={result.stderr.strip()[:800]}"
        )
    return pdf_path


def export_clean_html_attachment(html_text: str, source_path: Path, output_path: Path) -> Path:
    cleaned = re.sub(
        r'<section class="panel">\s*<h2>Lux / CCT / ADRC 散点</h2>.*?</section>',
        "",
        html_text,
        flags=re.DOTALL,
    )
    cleaned = re.sub(
        r'<section class="panel" style="margin-top:20px;">\s*<h2>需求映射与缺口</h2>.*?</section>',
        "",
        cleaned,
        flags=re.DOTALL,
    )
    attachment_overrides = """
    <style>
      body {
        background: #f7f4ee !important;
      }
      .wrap {
        width: min(1120px, calc(100% - 40px)) !important;
        padding: 24px 0 40px !important;
      }
      .hero, .trend-grid, .grid-2, .split-grid {
        grid-template-columns: 1fr 1fr !important;
      }
      .kpi-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
      }
      .grid-3, .viz-grid, .coverage-grid, .metric-row {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
      }
      .panel, .kpi, .status-card, figure, .chart-shell, .line-shell {
        background: #ffffff !important;
        box-shadow: none !important;
        backdrop-filter: none !important;
        border: 1px solid #ddd6cb !important;
      }
      .panel {
        border-radius: 18px !important;
        padding: 18px 20px !important;
      }
      .kpi {
        border-radius: 16px !important;
        padding: 14px 16px !important;
      }
      .donut-wrap {
        grid-template-columns: 160px 1fr !important;
      }
      .bars {
        height: 210px !important;
      }
      .bar-track {
        max-width: 48px !important;
      }
      h1 {
        font-size: 34px !important;
      }
      h2 {
        font-size: 20px !important;
      }
      .sub, .foot, .chart-note, figcaption {
        color: #5f574d !important;
      }
      .badge {
        background: #f2eee6 !important;
      }
      @media (max-width: 900px) {
        .hero, .trend-grid, .grid-2, .split-grid, .grid-3, .viz-grid, .kpi-grid, .coverage-grid, .metric-row {
          grid-template-columns: 1fr !important;
        }
        .donut-wrap {
          grid-template-columns: 1fr !important;
        }
      }
    </style>
    """
    cleaned = cleaned.replace("</head>", f"{attachment_overrides}\n</head>")
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(cleaned, encoding="utf-8")
    return output_path


def build_message(
    *,
    subject: str,
    from_addr: str,
    recipients: list[str],
    plain_text: str,
    html_body: str | None,
    attachments: list[tuple[str, bytes, str, str]],
    file_attachments: list[tuple[bytes, str, str]],
) -> EmailMessage:
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = from_addr
    message["To"] = ", ".join(recipients)
    message.set_content(plain_text)
    html_part = None
    if html_body:
        message.add_alternative(html_body, subtype="html")
        html_part = message.get_payload()[-1]
    if html_part is not None:
        for cid, data, mime_type, filename in attachments:
            maintype, subtype = mime_type.split("/", 1)
            html_part.add_related(
                data,
                maintype=maintype,
                subtype=subtype,
                cid=f"<{cid}>",
                filename=filename,
                disposition="inline",
            )
    for data, mime_type, filename in file_attachments:
        maintype, subtype = mime_type.split("/", 1)
        message.add_attachment(
            data,
            maintype=maintype,
            subtype=subtype,
            filename=filename,
        )
    return message


def send_message(
    *,
    host: str,
    port: int,
    username: str,
    password: str,
    use_ssl: bool,
    use_tls: bool,
    message: EmailMessage,
) -> None:
    if use_ssl:
        with smtplib.SMTP_SSL(host, port, timeout=30) as server:
            server.ehlo()
            if username:
                server.login(username, password)
            server.send_message(message)
        return

    with smtplib.SMTP(host, port, timeout=30) as server:
        server.ehlo()
        if use_tls:
            server.starttls()
            server.ehlo()
        if username:
            server.login(username, password)
        server.send_message(message)


def main() -> int:
    args = parse_args()
    env = load_env_defaults()

    html_path = Path(args.html_file).expanduser().resolve()
    if not html_path.exists():
        print(f"error=html_file_not_found:{html_path}", file=sys.stderr)
        return 1

    smtp_host = (args.smtp_host or env.get("EMAIL_SMTP_HOST") or "smtp.gmail.com").strip()
    smtp_port = int(args.smtp_port or env.get("EMAIL_SMTP_PORT") or 587)
    smtp_username = (args.smtp_username or env.get("EMAIL_SMTP_USERNAME") or "").strip()
    smtp_password = (args.smtp_password or env.get("EMAIL_SMTP_PASSWORD") or "").strip()
    from_addr = (args.from_addr or env.get("EMAIL_FROM_ADDR") or smtp_username).strip()
    recipients = resolve_recipients(list(args.to or []), env)
    use_ssl = bool(args.use_ssl or str(env.get("EMAIL_SMTP_USE_SSL", "")).strip().lower() in {"1", "true", "yes"})
    use_tls = False if args.no_tls else True

    if not smtp_host:
        print("error=missing_smtp_host", file=sys.stderr)
        return 1
    if not from_addr:
        print("error=missing_from_addr", file=sys.stderr)
        return 1
    if not recipients:
        print("error=missing_to_addrs", file=sys.stderr)
        return 1

    original_html = html_path.read_text(encoding="utf-8")
    preview_html, attachments = inline_local_images(original_html, html_path)
    file_paths: list[Path] = [Path(path).expanduser().resolve() for path in list(args.attach_file or [])]
    if args.export_html_attachment:
        html_output = (
            Path(args.html_attachment_output).expanduser().resolve()
            if args.html_attachment_output
            else html_path.with_name(f"{html_path.stem}_email.html")
        )
        file_paths.append(export_clean_html_attachment(original_html, html_path, html_output))
    if args.export_pdf:
        pdf_output = Path(args.pdf_output).expanduser().resolve() if args.pdf_output else html_path.with_suffix(".pdf")
        chrome_path = resolve_chrome_path(args.chrome_path)
        file_paths.append(export_pdf_from_html(html_path, pdf_output, chrome_path))
    resolved_summary = args.summary or build_auto_summary(original_html)
    plain_text = args.plain_text or build_plain_text(args.subject, html_path, resolved_summary, file_paths)
    file_attachments: list[tuple[bytes, str, str]] = []
    for path in file_paths:
        if not path.exists():
            print(f"error=attachment_not_found:{path}", file=sys.stderr)
            return 1
        mime_type, _ = mimetypes.guess_type(path.name)
        file_attachments.append((path.read_bytes(), mime_type or "application/octet-stream", path.name))
    if args.summary or args.export_pdf or args.export_html_attachment or file_paths:
        html_body = None
        attachments = []
    else:
        html_body = preview_html
    message = build_message(
        subject=args.subject,
        from_addr=from_addr,
        recipients=recipients,
        plain_text=plain_text,
        html_body=html_body,
        attachments=attachments,
        file_attachments=file_attachments,
    )

    print(f"html_file={html_path}")
    print(f"inline_image_count={len(attachments)}")
    print(f"attachment_count={len(file_attachments)}")
    print(f"recipient_count={len(recipients)}")
    print(f"smtp_host={smtp_host}")
    print(f"use_ssl={int(use_ssl)}")
    print(f"use_tls={int(use_tls)}")
    if args.dry_run:
        print("email_sent=0")
        print("dry_run=1")
        return 0

    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            send_message(
                host=smtp_host,
                port=smtp_port,
                username=smtp_username,
                password=smtp_password,
                use_ssl=use_ssl,
                use_tls=use_tls,
                message=message,
            )
            print("email_sent=1")
            print(f"email_subject={args.subject}")
            print(f"email_to={', '.join(recipients)}")
            return 0
        except (smtplib.SMTPException, OSError) as exc:
            last_error = exc
            if attempt >= 3:
                break
            time.sleep(min(8.0, attempt * 2))

    print("email_sent=0", file=sys.stderr)
    print(f"error={last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
