"""Basic tests for the brain module."""

import numpy as np
from ditlab.brain.qubits import QubitBrainState
from ditlab.brain.dynamics import apply_qubit_update
from ditlab.brain.perception import generate_perception
from ditlab.brain.metrics import compute_entropy


def test_qubit_initialisation() -> None:
    state = QubitBrainState.init_random(3)
    assert state.amplitudes.shape == (3, 2)
    # Check normalisation
    norms = np.linalg.norm(state.amplitudes, axis=1)
    assert np.allclose(norms, 1.0)


def test_qubit_update() -> None:
    state = QubitBrainState.init_random(2)
    updated = apply_qubit_update(state, "bias towards state 1")
    assert updated.amplitudes.shape == (2, 2)


def test_perception_generation() -> None:
    state = QubitBrainState.init_random(2)
    perception = generate_perception(state)
    assert "description" in perception
    assert "threat_level" in perception


def test_entropy_computation() -> None:
    state = QubitBrainState.init_random(2)
    entropy = compute_entropy(state)
    assert entropy >= 0.0