# 🧠 DevMemory

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-MVP-orange.svg)
[![GitHub stars](https://img.shields.io/github/stars/Artkill24/devmemory)](https://github.com/Artkill24/devmemory/stargazers)

**Never forget why you made that decision.**

Automatically track and document technical decisions by analyzing your Git commits. DevMemory creates a searchable timeline of "why" behind your code changes.

## 🎯 The Problem

After 6 months, nobody remembers:
- Why we chose Redis over Memcached
- The reasoning behind that workaround
- Who understands the authentication system

DevMemory preserves this context automatically.

## ✨ Features

- 🔍 **Auto-detection** - Scans commits for 9 decision types
- 💾 **SQLite Storage** - Lightweight, portable database
- 🎨 **Beautiful CLI** - Rich terminal interface
- 📊 **Analytics** - Statistics and insights
- 📄 **Export** - Generate Markdown documentation
- 🔎 **Search** - Find decisions by keyword

## 🚀 Quick Start
```bash
git clone https://github.com/Artkill24/devmemory.git
cd devmemory
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

python src/cli.py analyze --days 30
python src/cli.py list
📊 Decision Types
TypeKeywordsConfidenceDependency Addedadd, install, upgrade90%Architecture Changerefactor, redesign80%Workaroundhack, temporary85%Performanceoptimize, cache70%Security Fixvulnerability, CVE95%+ 4 more types...
📖 Usage
bash# Analyze repository
python src/cli.py analyze --days 365

# List all decisions
python src/cli.py list

# Search
python src/cli.py search "redis"

# Statistics
python src/cli.py stats

# Show details
python src/cli.py show 1

# Export to Markdown
python src/cli.py export --output DECISIONS.md
🎬 Example Output
DevMemory Decisions (2 shown)
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Date     ┃ Type               ┃ Author   ┃ Title        ┃ Hash   ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━┩
│ 2025-10  │ Architecture Change│ Dev      │ Switch to JWT│ 6387e8 │
│ 2025-10  │ Dependency Added   │ Dev      │ Add Redis    │ 2def04 │
└──────────┴────────────────────┴──────────┴──────────────┴────────┘
🤝 Contributing
Contributions welcome! See CONTRIBUTING.md
Ideas:

New decision patterns
Export formats (PDF, JSON)
Web interface
GitHub Actions integration

📄 License
MIT License - See LICENSE
🙏 Acknowledgments
Created as an experiment in solving real developer pain points using AI-assisted development.

Star ⭐ this repo if you find it useful!
