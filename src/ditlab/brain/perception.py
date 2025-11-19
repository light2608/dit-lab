"""Functions for generating perceived environment from brain state.

The perception functions interpret the measured qubit bits and associated
probabilities to produce a representation of what the agent believes its
environment looks like. These functions may also consider entropy or
overload metrics to adjust the richness of the perception.
"""

from typing import Dict

from .qubits import QubitBrainState


def generate_perception(state: QubitBrainState) -> Dict[str, str]:
    """Generate a minimal perceived environment description from brain state.

    Args:
        state: The current brain state.

    Returns:
        A dictionary describing the perceived environment.
    """
    bits, probs = state.measure()
    # Simple heuristic: count the number of bits measured as 1
    ones = bits.sum()
    if ones == 0:
        threat_level = "low"
        description = "calm and empty"
    elif ones == 1:
        threat_level = "medium"
        description = "minor disturbance"
    else:
        threat_level = "high"
        description = "significant activity"
    return {
        "description": description,
        "threat_level": threat_level,
        "self_state": "neutral",
    }