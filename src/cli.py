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

@cli.command()
@click.option('--days', default=1, help='Number of recent days')
def recent(days):
    """Show recent decisions (default: today)"""
    try:
        from datetime import timedelta
        dm = DevMemory()
        cutoff = datetime.now() - timedelta(days=days)
        decisions = dm.session.query(DecisionModel).filter(
            DecisionModel.created_at >= cutoff
        ).order_by(DecisionModel.created_at.desc()).all()
        
        if not decisions:
            console.print(f"📭 No decisions in the last {days} day(s)", style="yellow")
        else:
            console.print(f"\n🕐 Recent Decisions (last {days} day(s))\n", style="bold blue")
            for d in decisions:
                console.print(f"[cyan]{d.created_at.strftime('%H:%M')}[/cyan] "
                             f"[magenta]{d.decision_type.replace('_', ' ').title()}[/magenta]")
                console.print(f"  {d.title}")
        dm.close()
    except Exception as e:
        console.print(f"❌ Error: {e}", style="bold red")
        sys.exit(1)

@cli.command()
@click.option('--days', default=90, help='Number of days to show')
def timeline(days):
    """Show visual timeline of decisions"""
    try:
        from datetime import timedelta
        from collections import defaultdict
        
        dm = DevMemory()
        cutoff = datetime.now() - timedelta(days=days)
        decisions = dm.session.query(DecisionModel).filter(
            DecisionModel.created_at >= cutoff
        ).order_by(DecisionModel.created_at.asc()).all()
        
        if not decisions:
            console.print("No decisions in this time period", style="yellow")
            dm.close()
            return
        
        by_month = defaultdict(list)
        for d in decisions:
            month_key = d.created_at.strftime('%Y-%m')
            by_month[month_key].append(d)
        
        console.print(f"\n📅 Decision Timeline (last {days} days)\n", style="bold cyan")
        
        for month in sorted(by_month.keys()):
            month_decisions = by_month[month]
            month_name = datetime.strptime(month, '%Y-%m').strftime('%B %Y')
            
            console.print(f"\n{month_name}", style="bold yellow")
            console.print("─" * 60)
            
            for d in month_decisions:
                type_emoji = {
                    'dependency_added': '📦',
                    'architecture_change': '🏗️',
                    'security_fix': '🔒',
                    'performance_optimization': '⚡',
                    'workaround': '🔧',
                    'config_change': '⚙️',
                    'api_design': '🔌',
                    'database_schema': '🗄️'
                }.get(d.decision_type, '��')
                
                date_str = d.created_at.strftime('%d')
                console.print(
                    f"  {date_str} │ {type_emoji} {d.title[:50]}" + 
                    ("..." if len(d.title) > 50 else ""),
                    style="dim"
                )
        
        console.print(f"\n\nTotal: {len(decisions)} decisions", style="bold green")
        dm.close()
        
    except Exception as e:
        console.print(f"❌ Error: {e}", style="bold red")
        sys.exit(1)

@cli.command()
def summary():
    """Quick project overview with key metrics"""
    try:
        from collections import Counter
        dm = DevMemory()
        
        all_decisions = dm.session.query(DecisionModel).all()
        
        if not all_decisions:
            console.print("📭 No decisions tracked yet. Run 'analyze' first!", style="yellow")
            dm.close()
            return
        
        total = len(all_decisions)
        by_type = Counter(d.decision_type for d in all_decisions)
        authors = Counter(d.author for d in all_decisions)
        
        dates = [d.created_at for d in all_decisions]
        oldest = min(dates)
        newest = max(dates)
        days_span = (newest - oldest).days
        
        console.print("\n" + "="*60, style="bold cyan")
        console.print("📊 DevMemory Project Summary", style="bold cyan")
        console.print("="*60 + "\n", style="bold cyan")
        
        console.print(f"📦 Total Decisions: [bold]{total}[/bold]")
        console.print(f"📅 Tracking Period: {days_span} days ({oldest.strftime('%Y-%m-%d')} to {newest.strftime('%Y-%m-%d')})")
        console.print(f"👥 Contributors: {len(authors)}\n")
        
        console.print("🏆 Top Decision Types:", style="bold yellow")
        for dtype, count in by_type.most_common(3):
            emoji = {'dependency_added': '📦', 'architecture_change': '🏗️', 
                    'security_fix': '🔒', 'performance_optimization': '⚡'}.get(dtype, '📝')
            console.print(f"   {emoji} {dtype.replace('_', ' ').title()}: {count}")
        
        console.print(f"\n👤 Most Active:", style="bold yellow")
        top_author, top_count = authors.most_common(1)[0]
        console.print(f"   {top_author} ({top_count} decisions)")
        
        console.print("\n💡 Tip: Use 'timeline' for chronological view or 'export' for full report\n")
        
        dm.close()
    except Exception as e:
        console.print(f"❌ Error: {e}", style="bold red")
        sys.exit(1)

if __name__ == '__main__':
    cli()
