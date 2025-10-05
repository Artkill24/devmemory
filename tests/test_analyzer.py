import pytest
from src.analyzer.decision_detector import DecisionPatternAnalyzer
from datetime import datetime

def test_dependency_detection():
    analyzer = DecisionPatternAnalyzer()
    decision = analyzer.analyze_commit(
        commit_message="Add Redis for caching",
        files_changed=['requirements.txt'],
        commit_hash='abc123',
        author='Test',
        date=datetime.now()
    )
    assert decision is not None
    assert decision.type == 'dependency_added'
    assert decision.confidence > 0.5

def test_refactor_detection():
    analyzer = DecisionPatternAnalyzer()
    decision = analyzer.analyze_commit(
        commit_message="Refactor authentication system",
        files_changed=['auth.py'],
        commit_hash='def456',
        author='Test',
        date=datetime.now()
    )
    assert decision is not None
    assert decision.type == 'architecture_change'
