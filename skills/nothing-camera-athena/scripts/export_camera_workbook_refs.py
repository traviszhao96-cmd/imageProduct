#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List
from xml.etree import ElementTree as ET
from zipfile import ZipFile

NS = {
    "main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "rel": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}

OUTPUT_NAMES = {
    "General": "general.md",
    "Photo": "photo.md",
    "Video": "video.md",
    "性能": "performance.md",
}

CARRY_HEADERS = {
    "event_name",
    "key",
    "event_note",
    "key_note",
    "label",
    "label_note",
    "默认值",
    "备注",
}


@dataclass
class SheetTable:
    name: str
    description: str
    headers: List[str]
    rows: List[Dict[str, str]]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export Camera App SW埋点 workbook to markdown references.")
    parser.add_argument("--input", required=True, help="Path to the source xlsx file.")
    parser.add_argument("--output-dir", required=True, help="Directory to write markdown references into.")
    return parser.parse_args()


def parse_shared_strings(zf: ZipFile) -> List[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []

    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    strings = []
    for item in root.findall("main:si", NS):
        strings.append("".join(node.text or "" for node in item.iterfind(".//main:t", NS)))
    return strings


def cell_value(cell: ET.Element, shared_strings: List[str]) -> str:
    cell_type = cell.attrib.get("t")
    value = cell.find("main:v", NS)
    if cell_type == "s" and value is not None:
        return shared_strings[int(value.text or "0")]
    if cell_type == "inlineStr":
        return "".join(node.text or "" for node in cell.iterfind(".//main:t", NS))
    if value is not None:
        return value.text or ""
    return "".join(node.text or "" for node in cell.iterfind(".//main:t", NS))


def column_name(cell_ref: str) -> str:
    letters = []
    for char in cell_ref:
      if char.isalpha():
        letters.append(char)
      else:
        break
    return "".join(letters)


def load_workbook_sheets(xlsx_path: Path) -> Dict[str, List[Dict[str, str]]]:
    with ZipFile(xlsx_path) as zf:
        shared_strings = parse_shared_strings(zf)
        workbook = ET.fromstring(zf.read("xl/workbook.xml"))
        rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
        rel_map = {rel.attrib["Id"]: rel.attrib["Target"] for rel in rels}

        sheets: Dict[str, List[Dict[str, str]]] = {}
        for sheet in workbook.find("main:sheets", NS):
            sheet_name = sheet.attrib["name"]
            rel_id = sheet.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]
            target = "xl/" + rel_map[rel_id]
            root = ET.fromstring(zf.read(target))
            parsed_rows: List[Dict[str, str]] = []

            for row in root.findall(".//main:sheetData/main:row", NS):
                row_map: Dict[str, str] = {}
                for cell in row.findall("main:c", NS):
                    row_map[column_name(cell.attrib.get("r", ""))] = cell_value(cell, shared_strings).strip()
                parsed_rows.append(row_map)

            sheets[sheet_name] = parsed_rows

        return sheets


def sorted_columns(row_map: Dict[str, str]) -> List[str]:
    def key_fn(col: str) -> tuple[int, str]:
        number = 0
        for char in col:
            number = number * 26 + (ord(char.upper()) - 64)
        return number, col

    return sorted(row_map.keys(), key=key_fn)


def normalize_header(header: str) -> str:
    return header.strip()


def find_header_index(rows: List[Dict[str, str]]) -> int:
    for index, row in enumerate(rows):
        values = {normalize_header(value) for value in row.values() if value.strip()}
        if {"event_name", "key"} <= values:
            return index
        if "Vesion" in values:
            return index
    raise ValueError("Could not find header row")


def build_sheet_table(sheet_name: str, rows: List[Dict[str, str]]) -> SheetTable:
    header_index = find_header_index(rows)
    header_row = rows[header_index]
    header_columns = [col for col in sorted_columns(header_row) if header_row[col].strip()]
    headers = [normalize_header(header_row[col]) for col in header_columns]
    description = rows[header_index - 1].get("B", "").strip() if header_index > 0 else ""
    carry: Dict[str, str] = {}
    table_rows: List[Dict[str, str]] = []

    for row in rows[header_index + 1 :]:
        if not any(value.strip() for value in row.values()):
            continue

        current: Dict[str, str] = {}
        for col, header in zip(header_columns, headers):
            value = row.get(col, "").strip()
            if value:
                current[header] = value
                if header in CARRY_HEADERS:
                    carry[header] = value
            else:
                current[header] = carry.get(header, "") if header in CARRY_HEADERS else ""

        if any(value for value in current.values()):
            table_rows.append(current)

    return SheetTable(name=sheet_name, description=description, headers=headers, rows=table_rows)


def md_escape(text: str) -> str:
    if text is None:
        return ""
    return text.replace("|", "\\|").replace("\n", "<br>")


def render_table(headers: List[str], rows: List[Dict[str, str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(md_escape(row.get(header, "")) or " " for header in headers) + " |")
    return "\n".join(lines)


def write_sheet_reference(output_path: Path, source_path: Path, table: SheetTable) -> None:
    body = [
        f"# {table.name}",
        "",
        f"- Source workbook: `{source_path}`",
        f"- Extracted rows: `{len(table.rows)}`",
    ]
    if table.description:
        body.extend(["", "## Sheet Note", "", table.description])

    body.extend(["", "## Table", "", render_table(table.headers, table.rows), ""])
    output_path.write_text("\n".join(body), encoding="utf-8")


def build_history_table(rows: List[Dict[str, str]]) -> SheetTable:
    return build_sheet_table("History", rows)


def write_overview(output_path: Path, source_path: Path, tables: List[SheetTable], history_table: SheetTable) -> None:
    body = [
        "# Camera App SW埋点 Workbook Overview",
        "",
        f"- Source workbook: `{source_path}`",
        "- Generated by `scripts/export_camera_workbook_refs.py`",
        "",
        "## Sheet Index",
        "",
        "| sheet | purpose | reference | rows |",
        "| --- | --- | --- | --- |",
    ]

    for table in tables:
        purpose = table.description or "-"
        reference = OUTPUT_NAMES.get(table.name, "-")
        body.append(f"| {table.name} | {md_escape(purpose)} | `{reference}` | {len(table.rows)} |")

    body.extend(
        [
            "",
            "## History",
            "",
            render_table(history_table.headers, history_table.rows),
            "",
        ]
    )

    output_path.write_text("\n".join(body), encoding="utf-8")


def main() -> None:
    args = parse_args()
    source_path = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    workbook_rows = load_workbook_sheets(source_path)
    tables = [build_sheet_table(sheet_name, workbook_rows[sheet_name]) for sheet_name in OUTPUT_NAMES]
    history_table = build_history_table(workbook_rows["History"])

    for table in tables:
        write_sheet_reference(output_dir / OUTPUT_NAMES[table.name], source_path, table)

    write_overview(output_dir / "workbook-overview.md", source_path, tables, history_table)


if __name__ == "__main__":
    main()
