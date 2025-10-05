from src.analyzer.decision_detector import DecisionPatternAnalyzer
from datetime import datetime

analyzer = DecisionPatternAnalyzer()

# Test con i nostri commit reali
test_commits = [
    {
        'commit_message': 'Add Redis for caching session data',
        'files_changed': ['requirements.txt'],
        'commit_hash': 'abc123',
        'author': 'Test User',
        'date': datetime.now()
    },
    {
        'commit_message': 'Refactor authentication to use JWT tokens instead of sessions',
        'files_changed': ['config.yml', 'auth.py'],
        'commit_hash': 'def456',
        'author': 'Test User',
        'date': datetime.now()
    }
]

for commit in test_commits:
    print(f"\n{'='*60}")
    print(f"Testing: {commit['commit_message']}")
    print(f"Files: {commit['files_changed']}")
    
    decision = analyzer.analyze_commit(**commit)
    
    if decision:
        print(f"✅ DETECTED: {decision.type}")
        print(f"   Confidence: {decision.confidence:.0%}")
        print(f"   Indicators: {decision.indicators}")
    else:
        print("❌ NOT DETECTED - Testing patterns manually...")
        
        # Debug: Check each pattern
        message_lower = commit['commit_message'].lower()
        for pattern_name, pattern in analyzer.PATTERNS.items():
            keyword_matches = [kw for kw in pattern['keywords'] if kw in message_lower]
            if keyword_matches:
                print(f"   {pattern_name}: matched keywords {keyword_matches}")
