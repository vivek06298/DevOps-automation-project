# DevOps Automation Project

A beginner-friendly DevOps practice project using:

- Python
- Flask
- Bash scripting
- Git
- GitHub Actions

## Features

- Flask app with `/` and `/health` endpoints
- Bash scripts for setup, run, test, and health checks
- Git helper script for branch/commit/push automation
- Python log analysis tool
- GitHub Actions CI pipeline that runs tests automatically

## Project Structure

```bash
devops-automation-project/
├── app/
├── scripts/
├── tools/
├── tests/
├── .github/workflows/
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

```bash
chmod +x scripts/*.sh
./scripts/setup.sh
```

## Run the App

```bash
./scripts/run.sh
```

## Test the App

```bash
./scripts/test.sh
```

## Health Check

Open a second terminal and run:

```bash
./scripts/healthcheck.sh
```

## Generate Log Report

After hitting the app endpoints a few times:

```bash
source venv/bin/activate
python tools/log_report.py
```

## Git Helper

```bash
./scripts/git-helper.sh
```

## CI

GitHub Actions runs tests automatically on pushes and pull requests to `main`.

## What I Learned

- Automating environment setup with Bash
- Running tests through repeatable scripts
- Adding health checks to services
- Parsing logs with Python
- Building a simple CI workflow using GitHub Actions