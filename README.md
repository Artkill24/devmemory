# 🧠 DevMemory

**Never forget why you made that decision.**

DevMemory automatically tracks and documents the important decisions in your codebase by analyzing commits, pull requests, and code changes. It creates a searchable timeline of "why" that helps both current and future team members understand the context behind technical choices.

## 🎯 Problem

- "Why did we choose this library over alternatives?"
- "What was the reasoning behind this workaround?"
- "Who understands this legacy system?"

After months pass, this context disappears. DevMemory preserves it automatically.

## ✨ Features

- 🔍 **Automatic Analysis** - Scans commits and PRs for decision points
- 📊 **Decision Timeline** - Visual history of technical choices
- 🤖 **AI Summaries** - Generates human-readable decision records
- 🔎 **Smart Search** - Find decisions by keyword, author, or date
- 📝 **Zero Overhead** - No manual documentation required

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Initialize in your repo
python src/cli.py init

# Analyze recent commits
python src/cli.py analyze --since 30d

# List decisions
python src/cli.py list

# Search decisions
python src/cli.py search "redis"
```

## 📦 Installation

```bash
git clone https://github.com/yourusername/devmemory.git
cd devmemory
pip install -r requirements.txt
```

## 🔧 Configuration

Copy `.env.example` to `.env` and configure:

```env
GITHUB_TOKEN=your_token
GITHUB_REPO=owner/repo
ANTHROPIC_API_KEY=optional_for_ai_summaries
```

## 🏗️ Architecture

```
devmemory/
├── src/
│   ├── analyzer/     # Commit and PR analysis
│   ├── storage/      # SQLite database
│   ├── web/          # Web interface
│   └── ai/           # LLM-based summarization
└── tests/
```

## 🤝 Contributing

Contributions welcome! This is an experimental project to solve a real problem.

## 📄 License

MIT License - See LICENSE file

---

**Status**: 🚧 Early development - MVP in progress
