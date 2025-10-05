"""Export decisions to Markdown format"""

from devmemory import DevMemory
from datetime import datetime

def export_to_markdown(output_file='DECISIONS.md'):
    """Export all decisions to a Markdown file"""
    dm = DevMemory()
    
    # Get all decisions
    decisions = dm.session.query(dm.session.query(DecisionModel).statement.c).all()
    
    with open(output_file, 'w') as f:
        f.write(f"# Project Decisions\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"Total Decisions: {len(decisions)}\n\n")
        f.write("---\n\n")
        
        for d in decisions:
            f.write(f"## {d.title}\n\n")
            f.write(f"- **Type:** {d.decision_type.replace('_', ' ').title()}\n")
            f.write(f"- **Author:** {d.author}\n")
            f.write(f"- **Date:** {d.created_at.strftime('%Y-%m-%d')}\n")
            f.write(f"- **Commit:** `{d.commit_hash}`\n\n")
            f.write(f"### Summary\n\n{d.summary}\n\n")
            if d.reasoning:
                f.write(f"### Analysis\n\n{d.reasoning}\n\n")
            f.write("---\n\n")
    
    dm.close()
    print(f"Exported to {output_file}")

if __name__ == '__main__':
    export_to_markdown()
