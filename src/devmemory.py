"""DevMemory Core - Main integration module"""

import os
from datetime import datetime, timedelta
from pathlib import Path
from git import Repo
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from rich.console import Console
from rich.table import Table
from rich.progress import track

from storage.models import Base, Decision as DecisionModel
from analyzer.decision_detector import DecisionPatternAnalyzer, Decision

console = Console()

class DevMemory:
    """Main DevMemory application"""
    
    def __init__(self, repo_path='.', db_url='sqlite:///devmemory.db'):
        self.repo_path = repo_path
        self.repo = Repo(repo_path)
        self.analyzer = DecisionPatternAnalyzer()
        
        # Setup database
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        
        console.print(f"✅ DevMemory initialized at {repo_path}", style="green")
    
    def analyze_repository(self, days=30, force=False):
        """Analyze repository commits and extract decisions"""
        console.print(f"\n🔍 Analyzing last {days} days of commits...", style="bold blue")
        
        # Get commits
        since = datetime.now() - timedelta(days=days)
        commits = list(self.repo.iter_commits(since=since))
        
        console.print(f"Found {len(commits)} commits to analyze\n")
        
        decisions_found = 0
        decisions_saved = 0
        
        for commit in track(commits, description="Processing commits"):
            # Skip if already processed (unless force)
            if not force:
                existing = self.session.query(DecisionModel).filter_by(
                    commit_hash=commit.hexsha
                ).first()
                if existing:
                    continue
            
            # Analyze - FIX: Use correct parameter names!
            decision = self.analyzer.analyze_commit(
                commit_message=commit.message,
                files_changed=list(commit.stats.files.keys()),
                commit_hash=commit.hexsha,
                author=commit.author.name,
                date=commit.committed_datetime
            )
            
            if decision:
                decisions_found += 1
                
                # Save to database
                if self._save_decision(decision):
                    decisions_saved += 1
        
        console.print(f"\n✅ Analysis complete!", style="bold green")
        console.print(f"   Decisions found: {decisions_found}")
        console.print(f"   New decisions saved: {decisions_saved}\n")
        
        return decisions_saved
    
    def _save_decision(self, decision: Decision) -> bool:
        """Save decision to database"""
        try:
            db_decision = DecisionModel(
                commit_hash=decision.commit_hash,
                decision_type=decision.type,
                title=decision.title,
                summary=decision.summary,
                reasoning=f"Confidence: {decision.confidence:.0%}\nIndicators: {', '.join(decision.indicators)}",
                author=decision.author,
                created_at=decision.date,
                tags=','.join(decision.files_changed[:5])  # First 5 files as tags
            )
            
            self.session.add(db_decision)
            self.session.commit()
            return True
        except Exception as e:
            console.print(f"❌ Error saving decision: {e}", style="red")
            self.session.rollback()
            return False
    
    def list_decisions(self, limit=20, decision_type=None):
        """List all decisions from database"""
        query = self.session.query(DecisionModel)
        
        if decision_type:
            query = query.filter_by(decision_type=decision_type)
        
        decisions = query.order_by(DecisionModel.created_at.desc()).limit(limit).all()
        
        if not decisions:
            console.print("📭 No decisions found yet. Run 'analyze' first!", style="yellow")
            return
        
        # Create table
        table = Table(title=f"DevMemory Decisions ({len(decisions)} shown)")
        table.add_column("Date", style="cyan", width=12)
        table.add_column("Type", style="magenta", width=20)
        table.add_column("Author", style="blue", width=15)
        table.add_column("Title", style="green")
        table.add_column("Hash", style="dim", width=8)
        
        for d in decisions:
            table.add_row(
                d.created_at.strftime("%Y-%m-%d"),
                d.decision_type.replace('_', ' ').title(),
                d.author,
                d.title[:60] + "..." if len(d.title) > 60 else d.title,
                d.commit_hash[:8]
            )
        
        console.print(table)
    
    def search_decisions(self, query):
        """Search decisions by keyword"""
        decisions = self.session.query(DecisionModel).filter(
            DecisionModel.title.contains(query) |
            DecisionModel.summary.contains(query) |
            DecisionModel.tags.contains(query)
        ).all()
        
        if not decisions:
            console.print(f"🔍 No decisions found matching '{query}'", style="yellow")
            return
        
        console.print(f"\n🔎 Found {len(decisions)} decisions matching '{query}':\n", style="bold")
        
        for d in decisions:
            console.print(f"[cyan]{d.created_at.strftime('%Y-%m-%d')}[/cyan] "
                         f"[magenta]{d.decision_type.replace('_', ' ').title()}[/magenta]")
            console.print(f"  {d.title}")
            console.print(f"  by {d.author} ({d.commit_hash[:8]})")
            console.print()
    
    def get_decision_details(self, decision_id):
        """Get full details of a specific decision"""
        decision = self.session.query(DecisionModel).get(decision_id)
        
        if not decision:
            console.print(f"❌ Decision #{decision_id} not found", style="red")
            return
        
        console.print(f"\n{'='*60}", style="bold")
        console.print(f"Decision #{decision.id}: {decision.title}", style="bold green")
        console.print(f"{'='*60}\n", style="bold")
        
        console.print(f"[cyan]Type:[/cyan] {decision.decision_type.replace('_', ' ').title()}")
        console.print(f"[cyan]Author:[/cyan] {decision.author}")
        console.print(f"[cyan]Date:[/cyan] {decision.created_at.strftime('%Y-%m-%d %H:%M')}")
        console.print(f"[cyan]Commit:[/cyan] {decision.commit_hash}")
        console.print()
        
        console.print("[bold]Summary:[/bold]")
        console.print(decision.summary)
        console.print()
        
        if decision.reasoning:
            console.print("[bold]Analysis:[/bold]")
            console.print(decision.reasoning)
            console.print()
        
        if decision.tags:
            console.print(f"[cyan]Files:[/cyan] {decision.tags}")
    
    def get_statistics(self):
        """Get repository statistics"""
        total_decisions = self.session.query(DecisionModel).count()
        
        # Count by type
        from sqlalchemy import func
        type_counts = self.session.query(
            DecisionModel.decision_type,
            func.count(DecisionModel.id)
        ).group_by(DecisionModel.decision_type).all()
        
        console.print("\n📊 DevMemory Statistics\n", style="bold blue")
        console.print(f"Total Decisions: {total_decisions}\n")
        
        if type_counts:
            table = Table(title="Decisions by Type")
            table.add_column("Type", style="magenta")
            table.add_column("Count", style="cyan", justify="right")
            
            for dtype, count in sorted(type_counts, key=lambda x: x[1], reverse=True):
                table.add_row(dtype.replace('_', ' ').title(), str(count))
            
            console.print(table)
    
    def close(self):
        """Close database connection"""
        self.session.close()
