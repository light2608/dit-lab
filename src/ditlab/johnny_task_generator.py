"""Johnny Task Generator

This module provides a simple parser that ingests Johnny’s rants
and extracts actionable tasks based on key phrases. The intent is to
translate emotional feedback and stream‑of‑consciousness complaints
into concrete engineering tasks. While primitive, it demonstrates how
automated tooling could evolve to support cognitive project management.
"""

import re
from typing import List


def generate_tasks_from_rant(rant: str) -> List[str]:
    """Parse a rant and return a list of task descriptions.

    Args:
        rant: A string containing Johnny’s free‑form speech.

    Returns:
        A list of task descriptions derived from the rant.
    """
    tasks: List[str] = []
    # Split by sentence boundaries; basic heuristic
    sentences = re.split(r"[.!?]\s+", rant.strip())
    for sentence in sentences:
        s = sentence.lower().strip()
        if not s:
            continue
        # Basic pattern matching for known features
        if 'dashboard' in s:
            tasks.append('Design and implement the web dashboard UI')
        if 'interactive timeline' in s or 'timeline' in s:
            tasks.append('Implement snapshot timeline with controls to step, rewind and branch')
        if 'multiverse' in s:
            tasks.append('Add multiverse branching and comparative analysis tools')
        if 'snapshot' in s:
            tasks.append('Implement snapshot save/load functionality with state serialisation')
        if 'environment' in s:
            tasks.append('Build out environment stepping logic and state management')
        if 'brain' in s or 'qubit' in s:
            tasks.append('Develop qubit-based brain dynamics and measurement functions')
        if 'api' in s or 'endpoint' in s:
            tasks.append('Expose simulation control via REST API endpoints')
        if 'phase' in s or 'break it down' in s:
            tasks.append('Reorder project roadmap into manageable phases with milestones')
        # Add more patterns as needed
    return tasks


if __name__ == "__main__":
    # Example usage
    sample_rant = (
        "He wants everything at once: live interactive timeline, endless features, "
        "multiverse branching. I suggested we break it down into phases and focus on "
        "building the core environment and brain first before jumping to dashboards."
    )
    for task in generate_tasks_from_rant(sample_rant):
        print("-", task)