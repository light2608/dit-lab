"""Experiment script comparing chaotic and stable cognitive dynamics.

This example shows how to configure the brain dynamics to study the effects
of increased noise versus more stable update rules. The current script is a
placeholder and will be expanded as the simulation code evolves.
"""

import random
from typing import Tuple

from ditlab.env.simple_1d import Simple1DEnvironment
from ditlab.brain.qubits import QubitBrainState
from ditlab.llm.client_base import LLMClientBase
from ditlab.lab.controller import SimulationController


class DummyLLMClient(LLMClientBase):
    """A minimal LLM client returning random perceived environment."""

    def __call__(self, prompt: str) -> str -> str:
        # Randomly choose threat level and self state for demonstration
        threat = random.choice(["low", "medium", "high"])
        state = random.choice(["calm", "anxious", "excited", "neutral"])
        return (
            '{"qubit_update": "none", "perceived_environment": '
            '{"description": "dummy", "threat_level": "' + threat + '", '
            '"self_state": "' + state + '"}}'
        )


def run_experiment(noise_level: float, steps: int = 10) -> Tuple[int, dict]:
    """Run a simple experiment with a given noise level for a number of steps.

    Args:
        noise_level: A float indicating how noisy the dynamics should be.
        steps: The number of steps to run the simulation.

    Returns:
        A tuple containing the number of steps run and the last perceived
        environment as a dictionary.
    """
    env = Simple1DEnvironment()
    brain = QubitBrainState.init_random(4)
    llm = DummyLLMClient()
    controller = SimulationController(env, brain, llm)

    perceived = {}
    for _ in range(steps):
        state, perceived = controller.step_once()
    return steps, perceived


def main() -> None:
    print("Running chaos vs stability experiment...\n")
    steps, perceived = run_experiment(noise_level=0.5, steps=5)
    print(f"Ran {steps} steps. Final perceived environment: {perceived}")


if __name__ == "__main__":
    main()