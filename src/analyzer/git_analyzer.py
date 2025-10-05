"""Analyze git commits to extract decision points"""

from git import Repo
from datetime import datetime, timedelta
import re

class GitAnalyzer:
    def __init__(self, repo_path='.'):
        self.repo = Repo(repo_path)
    
    def get_recent_commits(self, days=7):
        """Get commits from last N days"""
        since = datetime.now() - timedelta(days=days)
        commits = list(self.repo.iter_commits(since=since))
        return commits
    
    def is_decision_commit(self, commit):
        """Detect if commit represents a decision"""
        message = commit.message.lower()
        
        # Decision indicators
        indicators = [
            'add', 'remove', 'switch to', 'migrate',
            'refactor', 'redesign', 'introduce',
            'fix', 'workaround', 'temporary'
        ]
        
        return any(ind in message for ind in indicators)
    
    def extract_decision_metadata(self, commit):
        """Extract metadata from a decision commit"""
        return {
            'hash': commit.hexsha[:8],
            'author': commit.author.name,
            'date': commit.committed_datetime,
            'message': commit.message,
            'files_changed': len(commit.stats.files),
        }

if __name__ == '__main__':
    analyzer = GitAnalyzer()
    commits = analyzer.get_recent_commits(30)
    print(f"Found {len(commits)} commits in last 30 days")
    
    decisions = [c for c in commits if analyzer.is_decision_commit(c)]
    print(f"Detected {len(decisions)} potential decisions")
