"""Metrics for evaluating the qubit brain state.

This module contains functions to compute entropy and other summary
statistics over the internal brain state. These metrics can be used
to infer stress levels, integration levels, or overload conditions.
"""

import numpy as np
from .qubits import QubitBrainState


def compute_entropy(state: QubitBrainState) -> float:
    """Compute a simple entropy metric for the brain state.

    The entropy is calculated as the sum of the Shannon entropy of each
    qubit’s probability distribution.

    Args:
        state: The current brain state.

    Returns:
        The total entropy across all qubits.
    """
    probs = np.abs(state.amplitudes) ** 2
    # Avoid log(0) by adding a small epsilon
    eps = 1e-12
    entropy = -np.sum(probs * np.log2(probs + eps))
    return float(entropy)