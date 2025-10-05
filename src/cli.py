#!/usr/bin/env python3
"""DevMemory CLI - Automatic project decision tracker"""

import click
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from devmemory import DevMemory
from storage.models import Decision as DecisionModel
from rich.console import Console

console = Console()

@click.group()
def cli():
    """🧠 DevMemory - Never forget why you made that decision"""
    pass

@cli.command()
@click.option('--days', default=30, help='Number of days to analyze')
@click.option('--force', is_flag=True, help='Reanalyze already processed commits')
def analyze(days, force):
    """Analyze repository commits and extract decisions"""
    try:
        dm = DevMemory()
        dm.analyze_repository(days=days, force=force)
        dm.close()
    except Exception as e:
        console.print(f"❌ Error: {e}", style="bold red")
        sys.exit(1)

@cli.command()
@click.option('--limit', default=20, help='Number of decisions to show')
@click.option('--type', 'decision_type', help='Filter by decision type')
def list(limit, decision_type):
    """List captured decisions"""
    try:
        dm = DevMemory()
        dm.list_decisions(limit=limit, decision_type=decision_type)
        dm.close()
    except Exception as e:
        console.print(f"❌ Error: {e}", style="bold red")
        sys.exit(1)

@cli.command()
@click.argument('query')
def search(query):
    """Search decisions by keyword"""
    try:
        dm = DevMemory()
        dm.search_decisions(query)
        dm.close()
    except Exception as e:
        console.print(f"❌ Error: {e}", style="bold red")
        sys.exit(1)

@cli.command()
@click.argument('decision_id', type=int)
def show(decision_id):
    """Show full details of a decision"""
    try:
        dm = DevMemory()
        dm.get_decision_details(decision_id)
        dm.close()
    except Exception as e:
        console.print(f"❌ Error: {e}", style="bold red")
        sys.exit(1)

@cli.command()
def stats():
    """Show repository statistics"""
    try:
        dm = DevMemory()
        dm.get_statistics()
        dm.close()
    except Exception as e:
        console.print(f"❌ Error: {e}", style="bold red")
        sys.exit(1)

@cli.command()
@click.option('--output', default='DECISIONS.md', help='Output file path')
def export(output):
    """Export decisions to Markdown file"""
    try:
        dm = DevMemory()
        decisions = dm.session.query(DecisionModel).order_by(
            DecisionModel.created_at.desc()
        ).all()
        
        with open(output, 'w', encoding='utf-8') as f:
            f.write("# Project Decisions Archive\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(f"**Total Decisions:** {len(decisions)}\n\n")
            
            # Group by type
            from collections import defaultdict
            by_type = defaultdict(list)
            for d in decisions:
                by_type[d.decision_type].append(d)
            
            f.write("## Summary by Type\n\n")
            for dtype, items in sorted(by_type.items(), key=lambda x: len(x[1]), reverse=True):
                f.write(f"- **{dtype.replace('_', ' ').title()}**: {len(items)}\n")
            
            f.write("\n---\n\n")
            f.write("## Detailed Decisions\n\n")
            
            for d in decisions:
                f.write(f"### {d.title}\n\n")
                f.write(f"- **Type:** {d.decision_type.replace('_', ' ').title()}\n")
                f.write(f"- **Author:** {d.author}\n")
                f.write(f"- **Date:** {d.created_at.strftime('%Y-%m-%d')}\n")
                f.write(f"- **Commit:** `{d.commit_hash}`\n\n")
                f.write("**Summary:**\n\n")
                f.write(f"{d.summary}\n\n")
                if d.reasoning:
                    f.write("**Analysis:**\n\n")
                    f.write(f"{d.reasoning}\n\n")
                f.write("---\n\n")
        
        dm.close()
        console.print(f"✅ Exported {len(decisions)} decisions to {output}", style="green")
    except Exception as e:
        console.print(f"❌ Error: {e}", style="bold red")
        sys.exit(1)

@cli.command()
def init():
    """Initialize DevMemory in current repository"""
    console.print("🎯 Initializing DevMemory...", style="bold green")
    try:
        dm = DevMemory()
        console.print("✅ DevMemory initialized successfully!", style="bold green")
        console.print("\nNext steps:", style="bold yellow")
        console.print("  1. Run: python src/cli.py analyze --days 30")
        console.print("  2. View: python src/cli.py list")
        console.print("  3. Export: python src/cli.py export")
        dm.close()
    except Exception as e:
        console.print(f"❌ Error: {e}", style="bold red")
        sys.exit(1)

if __name__ == '__main__':
    cli()
