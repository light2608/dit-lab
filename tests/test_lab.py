"""Basic tests for the lab controller."""

from ditlab.env.simple_1d import Simple1DEnvironment
from ditlab.brain.qubits import QubitBrainState
from ditlab.llm.client_base import LLMClientBase
from ditlab.lab.controller import SimulationController


class DummyLLM(LLMClientBase):
    def __call__(self, prompt: str) -> str:
        return '{"qubit_update": "none", "perceived_environment": {"description": "test", "threat_level": "low", "self_state": "calm"}}'


def test_simulation_step() -> None:
    env = Simple1DEnvironment(size=5)
    brain = QubitBrainState.init_random(2)
    llm = DummyLLM()
    controller = SimulationController(env, brain, llm)
    env_state, perceived = controller.step_once(action="right")
    assert env_state.agent_position == 1
    assert isinstance(perceived, dict)