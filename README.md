# 🧠 DevMemory

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Tests](https://github.com/Artkill24/devmemory/workflows/Tests/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-MVP-orange.svg)
[![GitHub stars](https://img.shields.io/github/stars/Artkill24/devmemory)](https://github.com/Artkill24/devmemory/stargazers)

**Never forget why you made that decision.**

Automatically track and document technical decisions by analyzing Git commits. Creates a searchable timeline of "why" behind your code.

## Quick Start
```bash
pip install -r requirements.txt
python src/cli.py analyze --days 30
python src/cli.py list
Commands

analyze - Scan repository for decisions
list - Show all decisions
search <keyword> - Find specific decisions
stats - View statistics
show <id> - Decision details
export - Generate Markdown report
recent - Today's decisions

Example
DevMemory Decisions
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Date     ┃ Type               ┃ Author   ┃ Title      ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━┩
│ 2025-10  │ Architecture       │ Dev      │ Switch JWT │
│ 2025-10  │ Dependency Added   │ Dev      │ Add Redis  │
└──────────┴────────────────────┴──────────┴────────────┘
MIT License | Contributing
