"""Qubit-based brain state representation.

This module defines a simple class to hold a collection of qubit-like
states using complex amplitude vectors. It provides initialisation
helpers and a measurement function that collapses the state into
classical bits and returns measurement probabilities.
"""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass, field
from typing import Any, List, Tuple


@dataclass
class QubitBrainState:
    """Represents the internal superposition-like state of the brain.

    Each qubit is represented by a two-dimensional complex vector whose
    squared magnitudes sum to 1. Collectively, these vectors can be
    manipulated by high-level update rules before being measured.
    """

    amplitudes: np.ndarray = field(default_factory=lambda: np.zeros((0, 2), dtype=np.complex128))

    @classmethod
    def init_random(cls, num_qubits: int) -> QubitBrainState:
        """Initialise a brain state with random complex amplitudes.

        Args:
            num_qubits: Number of qubits in the state.

        Returns:
            A new ``QubitBrainState`` with normalised random amplitudes.
        """
        amps = np.random.rand(num_qubits, 2) + 1j * np.random.rand(num_qubits, 2)
        # Normalise each qubit
        norms = np.linalg.norm(amps, axis=1, keepdims=True)
        amps = amps / norms
        return cls(amplitudes=amps)

    def measure(self) -> Tuple[np.ndarray, np.ndarray]:
        """Measure all qubits and return the resulting bits and probabilities.

        Each qubit collapses to 0 or 1 with probability proportional to
        the squared magnitude of the corresponding amplitude.

        Returns:
            A tuple ``(bits, probs)`` where ``bits`` is a 1D array of
            integers (0 or 1) and ``probs`` is the squared magnitude of
            the amplitudes.
        """
        probs = np.abs(self.amplitudes) ** 2  # shape (n,2)
        bits = (np.random.rand(self.amplitudes.shape[0]) < probs[:, 1]).astype(int)
        return bits, probs

    def copy(self) -> QubitBrainState:
        """Return a deep copy of the brain state."""
        return QubitBrainState(amplitudes=self.amplitudes.copy())