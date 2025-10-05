"""Database models for DevMemory"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Decision(Base):
    __tablename__ = 'decisions'
    
    id = Column(Integer, primary_key=True)
    commit_hash = Column(String(40), unique=True)
    decision_type = Column(String(50))  # dependency, refactor, workaround, etc.
    title = Column(String(200))
    summary = Column(Text)
    reasoning = Column(Text)
    author = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    tags = Column(Text)  # JSON array of tags
    
    def __repr__(self):
        return f"<Decision {self.title}>"

def init_db(database_url='sqlite:///devmemory.db'):
    """Initialize database"""
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    return engine
