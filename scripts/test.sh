#!/bin/bash
set -e

source venv/bin/activate

export PYTHONPATH=$(pwd)

echo "Running tests..."
pytest tests/ -v