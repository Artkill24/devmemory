# 🧠 DevMemory

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Tests](https://github.com/Artkill24/devmemory/workflows/Tests/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
[![GitHub stars](https://img.shields.io/github/stars/Artkill24/devmemory)](https://github.com/Artkill24/devmemory/stargazers)

**Never forget why you made that decision.**

Automatically track and document technical decisions by analyzing Git commits. Creates a searchable timeline of "why" behind your code.

## 🎬 See it in Action

[![asciicast](https://asciinema.org/a/t4kIvVJzvNDFEHjrewUsnlYYX.svg)](https://asciinema.org/a/t4kIvVJzvNDFEHjrewUsnlYYX)

*2-minute demo: analyze, search, timeline, and export*

## 🚀 Quick Start
```bash
git clone https://github.com/Artkill24/devmemory.git
cd devmemory
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Analyze your repository
python src/cli.py analyze --days 30
python src/cli.py summary
✨ Features

🔍 Auto-detection - 11 decision types (dependencies, refactors, security fixes...)
💾 Lightweight - SQLite database, no external services
🎨 Beautiful CLI - Rich terminal interface with colors and tables
📊 Analytics - Summary, timeline, and statistics
📄 Export - Generate Markdown documentation
🔎 Search - Find decisions instantly

�� Commands
CommandDescriptionanalyze --days NScan commits from last N dayslistShow all decisions in tablesummaryQuick project overview with metricstimelineVisual chronological view by monthsearch <keyword>Find specific decisionsshow <id>Full details of a decisionexportGenerate Markdown reportrecentToday's decisionsstatsStatistics by type
📊 Decision Types Detected
TypeKeywordsConfidence📦 Dependency Addedadd, install, upgrade90%🏗️ Architecture Changerefactor, redesign, migrate80%🔧 Workaroundhack, temporary, hotfix85%⚡ Performanceoptimize, cache, faster70%🔒 Security Fixvulnerability, CVE95%⚙️ Config Changesettings, environment60%🔌 API Designendpoint, route, interface75%🗄️ Database Schemamigration, table, column85%📝 Documentationdocs, readme40%🧪 Testingtest, unittest50%
🎯 Use Cases

Onboarding - New developers understand past decisions instantly
Documentation - Auto-generate decision logs and ADRs
Code Reviews - Provide context for why things exist
Technical Debt - Track workarounds and temporary solutions
Knowledge Transfer - Preserve team knowledge automatically

📈 Example Output
DevMemory Decisions (2 shown)
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━┓
┃ Date     ┃ Type               ┃ Author   ┃ Title      ┃ Hash   ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━┩
│ 2025-10  │ Architecture Change│ Dev      │ Switch JWT │ 6387e8 │
│ 2025-10  │ Dependency Added   │ Dev      │ Add Redis  │ 2def04 │
└──────────┴────────────────────┴──────────┴────────────┴────────┘
🤝 Contributing
Contributions welcome! See CONTRIBUTING.md
Ideas for contributions:

New decision patterns
Export formats (PDF, JSON)
Web interface
GitHub Actions integration
More tests

📄 License
MIT License - See LICENSE
🙏 Acknowledgments
Created as an experiment in solving real developer pain points using AI-assisted development.

⭐ Star this repo if DevMemory saved you from asking "why did we do this?"
