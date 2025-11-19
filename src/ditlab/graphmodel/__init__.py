"""Graph modelling subpackage.

The graph model package provides infrastructure for representing cognitive
timelines and DIT-inspired task graphs using NetworkX. Metrics such as
entropy and integration can be computed on these graphs.
"""

from .task_graph import TaskGraph  # noqa: F401

__all__ = ["TaskGraph"]