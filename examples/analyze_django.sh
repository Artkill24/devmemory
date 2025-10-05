#!/bin/bash
# Example: Analyze Django repository

git clone https://github.com/django/django.git /tmp/django
cd /tmp/django

python3 -m venv venv
source venv/bin/activate
pip install -r /path/to/devmemory/requirements.txt

python /path/to/devmemory/src/cli.py analyze --days 30
python /path/to/devmemory/src/cli.py stats
python /path/to/devmemory/src/cli.py export --output django_decisions.md
