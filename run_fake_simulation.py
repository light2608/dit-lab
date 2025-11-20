"""A simple standalone script to run the DIT Lab simulation without requiring
external LLM dependencies.  It demonstrates a basic loop over the
environment and brain using a stubbed LLM implementation.

Usage:
    PYTHONPATH=src python run_fake_simulation.py

The script runs a fixed number of steps in the Simple1DEnvironment using
a QubitBrainState and a FakeLLMClient that returns a constant response.
The true and perceived environment states are printed to the console.
"""

import json
from typing import Any, Dict

from ditlab.env.simple_1d import Simple1DEnvironment
from ditlab.brain.qubits import QubitBrainState
# We define a simple callable class for our fake LLM instead of
# inheriting from ditlab.llm.client_base.LLMClientBase to avoid
# importing the ``ditlab.llm`` package, which would in turn import
# the ``openai_client`` module and require the ``openai`` package.
# We avoid importing from ditlab.llm.__init__ or ditlab.llm.prompts to
# prevent inadvertently pulling in the OpenAI client and requiring the
# `openai` package, which is not available in this environment.
# Instead, we construct a simple fake perception directly without
# relying on those modules.


class FakeLLMClient:
    """A fake LLM client that returns a fixed perceived environment.

    This implementation ignores the prompt and always returns a JSON
    string describing a perceived environment with no qubit updates.
    It does not inherit from :class:`ditlab.llm.client_base.LLMClientBase`
    to avoid importing the ``openai_client`` module.
    """

    def __call__(self, prompt: str) -> str:
        # We ignore the prompt and return a constant perception.  In a
        # real implementation, you might analyse the prompt and return
        # something contextually relevant.
        response: Dict[str, Any] = {
            "qubit_update": "",  # no update to brain state
            "perceived_environment": {
                "description": "Agent hears nothing and sees nothing.",
                "threat_level": "none",
                "self_state": "neutral",
            },
        }
        return json.dumps(response)


def main() -> None:
    # Instantiate the environment and brain
    # Create a simple 1D environment.  The Simple1DEnvironment class
    # only accepts ``size`` as an argument; we configure the agent and
    # threat positions by modifying the state after instantiation.
    env = Simple1DEnvironment(size=10)
    # Set initial positions and parameters on the state
    env.state.agent_position = 0
    env.state.threat_position = 5
    env.state.light_level = 0.5
    env.state.noise_level = 0.0

    brain = QubitBrainState.init_random(num_qubits=4)
    llm = FakeLLMClient()

    # Run a fixed number of steps
    num_steps = 5
    for step in range(num_steps):
        # Step the environment with the default action
        env_state = env.step(action="stay")

        # Summarise the brain state
        bits, probs = brain.measure()

        # Call the fake LLM to get a dummy perception (we ignore the prompt)
        llm_response = llm("dummy prompt")
        parsed: Dict[str, Any] = json.loads(llm_response)
        perceived_env = parsed.get("perceived_environment", {})

        # Normally we would apply qubit updates here, but our FakeLLM
        # returns no updates, so the brain remains unchanged.

        # Print states
        print(f"Step {step}:")
        print("  True environment:", env_state.to_dict())
        print("  Perceived environment:", perceived_env)
        print("  Measured bits:", bits.tolist())
        print("  Probabilities:", probs.tolist())
        print()


if __name__ == "__main__":
    main()