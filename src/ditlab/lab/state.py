"""Simulation state and snapshot management.

This module defines data structures for encapsulating the complete
simulation state and provides a snapshot manager for rewinding and
branching timelines.
"""

from dataclasses import dataclass
from typing import Any, List, Tuple
from copy import deepcopy

from ditlab.env.base import EnvironmentState
from ditlab.brain.qubits import QubitBrainState


@dataclass
class FullState:
    """A complete snapshot of the environment and brain state."""

    env_state: EnvironmentState
    brain_state: QubitBrainState
    time_step: int


class SnapshotManager:
    """Manage a timeline of simulation snapshots with branching support."""

    def __init__(self) -> None:
        self.history: List[FullState] = []
        self.current_index: int = -1
        self.branches: List[List[FullState]] = []

    def save(self, env_state: EnvironmentState, brain_state: QubitBrainState, time_step: int) -> None:
        """Append a new snapshot to the current timeline."""
        state = FullState(deepcopy(env_state), deepcopy(brain_state), time_step)
        self.history.append(state)
        self.current_index = len(self.history) - 1

    def rewind(self, index: int = None) -> FullState:
        """Return an earlier snapshot from the history without removing it.

        Args:
            index: Optional index to rewind to. Defaults to the previous
                snapshot in the history.

        Returns:
            The snapshot at the specified index.
        """
        if not self.history:
            raise IndexError("No snapshots available to rewind to.")
        if index is None:
            index = max(0, self.current_index - 1)
        self.current_index = index
        state = self.history[self.current_index]
        return deepcopy(state)

    def branch(self) -> None:
        """Start a new branch from the current state.

        The current history is copied to the branches list, and a fresh
        history is started for the new branch.
        """
        self.branches.append(self.history[: self.current_index + 1])
        self.history = []
        self.current_index = -1