#!/bin/bash
set -e

URL="http://127.0.0.1:5000/health"

echo "Checking application health at $URL ..."
curl -f "$URL"

echo ""
echo "Health check passed."