"""Smart Decision Pattern Analyzer - Detects different types of technical decisions"""

import re
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Decision:
    """Represents a detected decision"""
    type: str
    confidence: float
    title: str
    summary: str
    commit_hash: str
    author: str
    date: datetime
    files_changed: List[str]
    indicators: List[str]

class DecisionPatternAnalyzer:
    """Analyzes commits to detect and classify technical decisions"""
    
    PATTERNS = {
        'dependency_added': {
            'keywords': ['add', 'install', 'upgrade', 'bump'],
            'files': ['requirements.txt', 'package.json', 'Gemfile', 'pom.xml', 'build.gradle', 'go.mod', 'Cargo.toml'],
            'weight': 0.9
        },
        'dependency_removed': {
            'keywords': ['remove', 'delete', 'uninstall', 'drop'],
            'files': ['requirements.txt', 'package.json', 'Gemfile'],
            'weight': 0.9
        },
        'architecture_change': {
            'keywords': ['refactor', 'restructure', 'redesign', 'migrate', 'rewrite', 'architecture'],
            'weight': 0.8
        },
        'workaround': {
            'keywords': ['workaround', 'hack', 'temporary', 'quick fix', 'hotfix', 'patch', 'band-aid'],
            'weight': 0.85
        },
        'performance_optimization': {
            'keywords': ['optimize', 'performance', 'speed up', 'cache', 'faster', 'improve', 'efficient'],
            'weight': 0.7
        },
        'security_fix': {
            'keywords': ['security', 'vulnerability', 'cve', 'exploit', 'xss', 'sql injection', 'csrf'],
            'weight': 0.95
        },
        'config_change': {
            'keywords': ['config', 'configuration', 'settings', 'environment', 'env'],
            'files': ['.env', 'config.yml', 'settings.py', 'application.properties', 'appsettings.json'],
            'weight': 0.6
        },
        'api_design': {
            'keywords': ['api', 'endpoint', 'route', 'interface', 'contract', 'rest', 'graphql'],
            'weight': 0.75
        },
        'database_schema': {
            'keywords': ['migration', 'schema', 'table', 'column', 'index', 'database'],
            'files': ['migrations/', 'schema.sql', 'alembic/'],
            'weight': 0.85
        },
        'testing': {
            'keywords': ['test', 'testing', 'unittest', 'integration test', 'e2e'],
            'files': ['test_', '_test.py', 'spec.js', '.test.'],
            'weight': 0.5
        },
        'documentation': {
            'keywords': ['docs', 'documentation', 'readme', 'comment'],
            'files': ['README', 'docs/', '.md'],
            'weight': 0.4
        }
    }
    
    def analyze_commit(self, commit_message: str, files_changed: List[str], 
                       commit_hash: str, author: str, date: datetime) -> Optional[Decision]:
        """Analyze a single commit and detect if it's a decision"""
        
        message_lower = commit_message.lower()
        decisions_detected = []
        
        for decision_type, pattern in self.PATTERNS.items():
            score = 0.0
            indicators = []
            
            # Check keywords
            keyword_matches = [kw for kw in pattern['keywords'] if kw in message_lower]
            if keyword_matches:
                score += pattern['weight']
                indicators.append(f"keywords: {', '.join(keyword_matches)}")
            
            # Check file patterns
            if 'files' in pattern:
                file_matches = [f for f in files_changed 
                               for pattern_file in pattern['files'] 
                               if pattern_file in f]
                if file_matches:
                    score += 0.5
                    indicators.append(f"files: {', '.join(file_matches[:3])}")
            
            # Lower threshold for important decisions
            threshold = 0.3 if decision_type in ['security_fix', 'architecture_change', 'workaround'] else 0.4
            
            if score >= threshold:
                decisions_detected.append({
                    'type': decision_type,
                    'score': min(score, 1.0),
                    'indicators': indicators
                })
        
        if decisions_detected:
            best = max(decisions_detected, key=lambda x: x['score'])
            
            return Decision(
                type=best['type'],
                confidence=best['score'],
                title=self._generate_title(commit_message),
                summary=commit_message.strip(),
                commit_hash=commit_hash,
                author=author,
                date=date,
                files_changed=files_changed,
                indicators=best['indicators']
            )
        
        return None
    
    def _generate_title(self, commit_message: str) -> str:
        """Extract a clean title from commit message"""
        first_line = commit_message.split('\n')[0]
        first_line = re.sub(r'^(feat|fix|docs|style|refactor|test|chore):\s*', '', first_line, flags=re.IGNORECASE)
        return first_line[:100]
    
    def batch_analyze(self, commits: List[Dict]) -> List[Decision]:
        """Analyze multiple commits and return detected decisions"""
        decisions = []
        
        for commit in commits:
            decision = self.analyze_commit(
                commit_message=commit.get('message', ''),
                files_changed=commit.get('files', []),
                commit_hash=commit.get('hash', ''),
                author=commit.get('author', ''),
                date=commit.get('date', datetime.now())
            )
            
            if decision:
                decisions.append(decision)
        
        return decisions
