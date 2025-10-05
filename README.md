# 🧠 DevMemory

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Tests](https://github.com/Artkill24/devmemory/workflows/Tests/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
[![GitHub stars](https://img.shields.io/github/stars/Artkill24/devmemory)](https://github.com/Artkill24/devmemory/stargazers)

**Never forget why you made that decision.**

Automatically track and document technical decisions by analyzing Git commits. Creates a searchable timeline of "why" behind your code.

## 🎬 See it in Action

[![asciicast](https://asciinema.org/a/IL_TUO_ID.svg)](https://asciinema.org/a/IL_TUO_ID)

*2-minute demo showing analysis, search, and export*

## 🚀 Quick Start
```bash
git clone https://github.com/Artkill24/devmemory.git
cd devmemory
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Analyze your repo
python src/cli.py analyze --days 30
python src/cli.py summary
✨ Features

🔍 Auto-detection - 11 decision types (dependencies, refactors, security fixes...)
💾 Lightweight - SQLite database, no external services
🎨 Beautiful CLI - Rich terminal interface with colors and tables
📊 Analytics - Summary, timeline, and statistics
📄 Export - Generate Markdown documentation
🔎 Search - Find decisions instantly

📖 Commands
CommandDescriptionanalyzeScan repository for decisionslistShow all decisions in a tablesummaryQuick project overviewtimelineVisual chronological viewsearch <keyword>Find specific decisionsshow <id>Detailed decision viewexportGenerate Markdown reportrecentToday's decisions
📊 Decision Types Detected
📦 Dependency Changes • 🏗️ Architecture • 🔧 Workarounds • ⚡ Performance
🔒 Security Fixes • ⚙️ Config • 🔌 API Design • 🗄️ Database • 📝 Documentation
🎯 Use Cases

Onboarding - New developers understand past decisions
Documentation - Auto-generate decision logs
Code Reviews - Context for why things exist
Technical Debt - Track workarounds and quick fixes
Knowledge Transfer - Preserve team knowledge

🤝 Contributing
Contributions welcome! See CONTRIBUTING.md
📄 License
MIT License - See LICENSE

⭐ Star this repo if DevMemory helped you!
