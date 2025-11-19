"""Experiment definitions for DIT Lab.

This module contains classes and functions for defining high-level
experiments. An experiment encapsulates the environment, brain,
controller, and parameter settings for an experimental run.
"""

from dataclasses import dataclass
from typing import Optional, Any

from ditlab.config.schemas import LabConfig
from ditlab.env.simple_1d import Simple1DEnvironment
from ditlab.brain.qubits import QubitBrainState
from ditlab.llm.client_base import LLMClientBase
from ditlab.llm.openai_client import OpenAIClient
from ditlab.lab.controller import SimulationController


@dataclass
class Experiment:
    """A runnable experiment with configured components."""

    config: LabConfig
    llm_client: Optional[LLMClientBase] = None

    def create_controller(self) -> SimulationController:
        """Create a simulation controller from the experiment config."""
        # Instantiate environment
        if self.config.environment.env_type == "simple_1d":
            env = Simple1DEnvironment(size=self.config.environment.size)
        else:
            raise ValueError(f"Unknown environment type: {self.config.environment.env_type}")
        # Instantiate brain
        brain = QubitBrainState.init_random(self.config.brain.num_qubits)
        # Instantiate LLM client
        llm = (
            self.llm_client
            if self.llm_client is not None
            else OpenAIClient(model_name=self.config.llm.model_name, temperature=self.config.llm.temperature)
        )
        return SimulationController(env, brain, llm)