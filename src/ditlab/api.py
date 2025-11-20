"""FastAPI interface for the DIT Lab simulator.

This module exposes a minimal REST API that wraps the core simulation
engine so it can be driven over HTTP. This allows the cognitive
simulator to be surfaced as a live application for testing and
interaction without requiring direct Python execution.

The API defines a handful of endpoints:

```
POST /reset
    Reset the simulation to its initial state.

POST /step
    Advance the simulation by one step. Accepts an optional
    ``action`` field in the JSON body to control the agent's movement.

GET /state
    Retrieve the current true environment state and the brain's
    perceived environment from the last step.
```

Under the hood the API holds global references to an environment,
a brain state and a simulation controller. A very simple
``FakeLLMClient`` is provided which returns a deterministic update and
perceived environment so that the API can be exercised without an
external LLM dependency. Once integrated with a real LLM client the
``FakeLLMClient`` can be replaced with an instance of
``OpenAIClient`` or another concrete implementation.
"""

from __future__ import annotations

from typing import Dict, Any, Optional

from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel

from .env.simple_1d import Simple1DEnvironment
from .brain.qubits import QubitBrainState
from .brain.perception import generate_perception
from .llm.client_base import LLMClientBase
from .lab.controller import SimulationController


class FakeLLMClient(LLMClientBase):
    """A dummy LLM client used for local testing.

    Instead of calling an external language model, this fake client
    simply generates a fixed update instruction and perceived
    environment description based on the measured qubit bits.
    """

    def __call__(self, prompt: str) -> str:
        # We don't parse the prompt here. In a real implementation,
        # the prompt would be inspected to tailor the response.
        # Instead, we return a JSON string with a static qubit update
        # and a very basic perceived environment.
        return (
            '{"qubit_update": "decohere", "perceived_environment": '
            '{"description": "testing", "threat_level": "unknown", "self_state": "neutral"}}'
        )


class StepRequest(BaseModel):
    """Schema for the request body of the /step endpoint."""
    action: Optional[str] = None


class StateResponse(BaseModel):
    """Schema for the response body of the /state endpoint."""
    env_state: Dict[str, Any]
    perceived: Dict[str, Any]


# Instantiate the core components. In a more advanced setup these
# would be created per-session or stored in a database. For this
# initial API we maintain a single global simulation.
_env = Simple1DEnvironment(size=10)
_brain = QubitBrainState.init_random(num_qubits=3)
_llm: LLMClientBase = FakeLLMClient()
_controller = SimulationController(env=_env, brain=_brain, llm=_llm)

app = FastAPI(title="DIT Lab Simulator API", version="0.0.1")


@app.post("/reset")
def reset_simulation() -> StateResponse:
    """Reset the global simulation state and return the initial state."""
    global _env, _brain, _controller
    _env.reset()
    _brain = QubitBrainState.init_random(num_qubits=3)
    _controller = SimulationController(env=_env, brain=_brain, llm=_llm)
    env_state, _ = _controller.step_once(action="stay")
    perceived = generate_perception(_controller.brain)
    return StateResponse(env_state=env_state.to_dict(), perceived=perceived)


@app.post("/step")
def step_simulation(req: StepRequest = Body(default_factory=StepRequest)) -> StateResponse:
    """Advance the simulation by one step and return the updated states."""
    if not _controller:
        raise HTTPException(status_code=500, detail="Simulation controller not initialised")
    env_state, perceived_llm = _controller.step_once(action=req.action)
    # The LLM response may return an empty perceived environment; if so
    # we fall back to a heuristic perception from the brain alone.
    if not perceived_llm:
        perceived_llm = generate_perception(_controller.brain)
    return StateResponse(env_state=env_state.to_dict(), perceived=perceived_llm)


@app.get("/state")
def get_state() -> StateResponse:
    """Return the current true and perceived environment states."""
    if not _controller:
        raise HTTPException(status_code=500, detail="Simulation controller not initialised")
    env_state = _controller.env.state
    # We'll derive perceived environment from the latest brain state via heuristic
    perceived = generate_perception(_controller.brain)
    return StateResponse(env_state=env_state.to_dict(), perceived=perceived)