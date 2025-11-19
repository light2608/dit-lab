"""Brain subpackage.

This package contains classes and functions implementing the cognitive engine
of the DIT Lab simulation. The core concept is a state represented by
superposition-like variables (qubits) together with dynamics, perception
functions, and metrics.
"""

from .qubits import QubitBrainState  # noqa: F401
from .dynamics import apply_qubit_update  # noqa: F401
from .perception import generate_perception  # noqa: F401
from .metrics import compute_entropy  # noqa: F401

__all__ = [
    "QubitBrainState",
    "apply_qubit_update",
    "generate_perception",
    "compute_entropy",
]