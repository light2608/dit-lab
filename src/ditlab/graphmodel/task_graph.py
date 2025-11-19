"""Task graph representation and utilities.

This module defines a simple wrapper around a NetworkX graph to represent
DIT-style cognitive timelines and to compute useful metrics. The task
graph can be extended with attributes on nodes and edges for more
complex models.
"""

from __future__ import annotations

import networkx as nx
from typing import Any, Iterable, Optional


class TaskGraph:
    """A wrapper class for a directed graph representing cognitive tasks."""

    def __init__(self) -> None:
        self.graph = nx.DiGraph()

    def add_task(self, task_id: Any, **attrs: Any) -> None:
        """Add a task node to the graph."""
        self.graph.add_node(task_id, **attrs)

    def add_dependency(self, from_task: Any, to_task: Any, **attrs: Any) -> None:
        """Add a directed edge representing a dependency between tasks."""
        self.graph.add_edge(from_task, to_task, **attrs)

    def tasks(self) -> Iterable[Any]:  # noqa: D401
        """Return an iterable over the task nodes."""
        return self.graph.nodes()

    def dependencies(self) -> Iterable[tuple]:  # noqa: D401
        """Return an iterable over the dependency edges."""
        return self.graph.edges()

    def entropy(self) -> float:
        """Compute an entropy-like metric for the task graph.

        This is a placeholder implementation that returns zero. Future
        versions will incorporate actual entropy computations based on
        edge weights and node distributions.
        """
        return 0.0