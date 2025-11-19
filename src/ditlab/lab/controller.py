"""Simulation controller for DIT Lab.

This module defines the :class:`SimulationController`, which coordinates
the interactions between the environment, brain, and LLM to run the
simulation step by step. It uses the functions in the ``brain`` and
``llm`` modules to update the state and produce perceptions.
"""

from typing import Tuple, Dict, Any

from ditlab.env.base import BaseEnvironment, EnvironmentState
from ditlab.brain.qubits import QubitBrainState
from ditlab.brain.dynamics import apply_qubit_update
from ditlab.brain.perception import generate_perception
from ditlab.llm.client_base import LLMClientBase
from ditlab.llm.prompts import build_prompt, parse_response
from ditlab.lab.state import SnapshotManager


class SimulationController:
    """Coordinates a simulation of environment, brain, and LLM."""

    def __init__(self, env: BaseEnvironment, brain: QubitBrainState, llm: LLMClientBase) -> None:
        self.env = env
        self.brain = brain
        self.llm = llm
        self.time_step = 0
        self.snapshots = SnapshotManager()

    def step_once(self, action: Any = None) -> Tuple[EnvironmentState, Dict[str, Any]]:
        """Advance the simulation by one time step.

        Args:
            action: Optional action for the agent to take in the environment.

        Returns:
            A tuple ``(env_state, perceived_env)`` where ``env_state`` is
            the true state of the environment after stepping, and
            ``perceived_env`` is the brain's perceived environment as
            produced by the LLM.
        """
        # 1. Update environment according to action
        env_state = self.env.step(action if action is not None else "stay")

        # 2. Summarise brain state for the prompt
        bits, probs = self.brain.measure()
        brain_summary = {
            "measured_bits": bits.tolist(),
            "probabilities": probs.tolist(),
        }

        # 3. Build and send prompt to the LLM
        prompt = build_prompt(env_state.to_dict(), brain_summary)
        llm_response = self.llm(prompt)

        # 4. Parse LLM response
        response_dict = parse_response(llm_response)
        update_instr = response_dict.get("qubit_update", "")
        perceived_env = response_dict.get("perceived_environment", {})

        # 5. Apply update to brain state
        self.brain = apply_qubit_update(self.brain, update_instr)

        # 6. Save snapshot
        self.snapshots.save(env_state, self.brain, self.time_step)
        self.time_step += 1

        return env_state, perceived_env