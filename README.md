# 🧠 DevMemory

**Never forget why you made that decision.**

DevMemory automatically tracks and documents important decisions in your codebase by analyzing commits. It creates a searchable timeline that helps both current and future team members understand the context behind technical choices.

## 🎯 The Problem We Solve

- "Why did we choose Redis over Memcached?"
- "What was the reasoning behind this workaround?"
- "Who understands the authentication system?"

After 6 months, context disappears. DevMemory preserves it automatically.

## ✨ Features

- 🔍 **Automatic Analysis** - Scans commits for decision patterns
- 📊 **9 Decision Types** - Dependencies, refactors, workarounds, security fixes, etc.
- 🎯 **Smart Detection** - Keyword + file pattern matching with confidence scoring
- 💾 **SQLite Storage** - Lightweight, portable database
- 🎨 **Beautiful CLI** - Rich terminal interface with tables and colors
- 🔎 **Search & Filter** - Find decisions by keyword, type, or author

## 🚀 Quick Start
```bash
# Clone and install
git clone https://github.com/yourusername/devmemory.git
cd devmemory
pip install -r requirements.txt

# Analyze your repository
python src/cli.py analyze --days 30

# View decisions
python src/cli.py list

# Search
python src/cli.py search "redis"

# Statistics
python src/cli.py stats

# Details
python src/cli.py show 1
📊 Decision Types Detected
TypeKeywordsExamplesDependency Addedadd, install, upgradeAdding Redis, upgrading DjangoArchitecture Changerefactor, redesign, migrateMoving to microservicesWorkaroundhack, temporary, hotfixQuick fix for memory leakPerformanceoptimize, cache, fasterAdding caching layerSecurity Fixsecurity, vulnerabilityPatching XSS vulnerabilityConfig Changeconfig, settingsUpdating environment variablesAPI Designendpoint, route, interfaceNew REST endpointsDatabase Schemamigration, schema, tableAdding user tableDependency Removedremove, uninstallDropping unused library
🏗️ Architecture
devmemory/
├── src/
│   ├── analyzer/
│   │   ├── git_analyzer.py       # Git repository scanner
│   │   └── decision_detector.py  # Pattern matching engine
│   ├── storage/
│   │   └── models.py             # SQLAlchemy models
│   ├── devmemory.py              # Core integration
│   └── cli.py                    # Command-line interface
├── tests/
└── devmemory.db                  # SQLite database (created on first run)
🧪 How It Works

Scans Git History - Analyzes commit messages and changed files
Pattern Matching - Detects keywords and file patterns
Confidence Scoring - Calculates decision confidence (0-100%)
Stores Context - Saves to SQLite with full metadata
Rich Queries - Search, filter, and explore decisions

📈 Example Output
DevMemory Decisions (2 shown)
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Date       ┃ Type               ┃ Author       ┃ Title          ┃ Hash   ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ 2025-10-05 │ Architecture Change│ Developer    │ Switch to JWT  │ 6387e8 │
│ 2025-10-05 │ Dependency Added   │ Developer    │ Add Redis      │ 2def04 │
└────────────┴────────────────────┴──────────────┴────────────────┴────────┘
🤝 Contributing
This is an experimental project solving a real problem. Contributions welcome!
📄 License
MIT License

Created with Claude - An AI assistant experiment in solving developer pain points
