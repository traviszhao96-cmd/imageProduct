#!/bin/bash
# Wrapper: runs athena_query_cli.py with the boto3 venv + nothing profile
# Usage: scripts/athena_query.sh smoke
#        scripts/athena_query.sh query --sql "SELECT ..."
#        scripts/athena_query.sh describe --table data_mobile_behavior
# 印度数据: REGION=ap-south-1 scripts/athena_query.sh query --sql "..."

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_PYTHON="/tmp/athena-boto3-venv/bin/python3"

if [ ! -f "$VENV_PYTHON" ]; then
    echo "❌ boto3 venv not found at $VENV_PYTHON" >&2
    echo "   创建 venv: python3 -m venv /tmp/athena-boto3-venv && /tmp/athena-boto3-venv/bin/pip3 install boto3 awscli" >&2
    exit 1
fi

# Default profile and region
PROFILE="${AWS_PROFILE:-nothing}"
REGION="${REGION:-eu-north-1}"

# Pass profile/region as regular args AFTER the subcommand
exec "$VENV_PYTHON" "$SCRIPT_DIR/athena_query_cli.py" "$@" --profile "$PROFILE" --region "$REGION"
