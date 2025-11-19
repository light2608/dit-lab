"""Minimal CLI demo for DIT Lab.

This script demonstrates how to instantiate a simple environment and brain,
perform a single update step via the lab controller, and display the true
environment state alongside the perceived environment reported by the
brain/LLM. The module imports are currently stubs; functionality will be
added incrementally.
"""

from ditlab.env.simple_1d import Simple1DEnvironment
from ditlab.brain.qubits import QubitBrainState
from ditlab.llm.client_base import LLMClientBase
from ditlab.lab.controller import SimulationController


def main() -> None:
    # Initialize environment and brain
    env = Simple1DEnvironment()
    brain = QubitBrainState.init_random(4)

    # Stub LLM client – this will need to be replaced with a real implementation
    class DummyLLMClient(LLMClientBase):
        def __call__(self, prompt: str) -> str:  # noqa: D401
            """Return a dummy JSON payload for testing."""
            return '{"qubit_update": "none", "perceived_environment": {"description": "empty", "threat_level": "low", "self_state": "neutral"}}'

    llm = DummyLLMClient()

    # Create simulation controller
    controller = SimulationController(env, brain, llm)

    # Perform a single step
    state, perceived = controller.step_once()

    # Display results
    print("True environment:", state)
    print("Perceived environment:", perceived)


if __name__ == "__main__":
    main()