"""Prompt building utilities for the LLM node.

This module contains helper functions to assemble prompts for the LLM
client from the environment and brain state. It also provides
parsing helpers to interpret the model response.
"""

import json
from typing import Dict, Tuple


def build_prompt(env_state: Dict[str, any], brain_summary: Dict[str, any]) -> str:
    """Build a string prompt from environment and brain summaries.

    Args:
        env_state: A dictionary describing the true environment state.
        brain_summary: A dictionary summarising the brain state (e.g., qubit
            measurement bits and probabilities).

    Returns:
        A formatted prompt string for the LLM.
    """
    return (
        "You are a cognitive modeling assistant.\n"
        "True environment state (JSON):\n"
        f"{json.dumps(env_state, indent=2)}\n"
        "Brain summary (JSON):\n"
        f"{json.dumps(brain_summary, indent=2)}\n"
        "Return a JSON object with keys: 'qubit_update' (string)
        and 'perceived_environment' (an object describing the perceived
        environment)."
    )


def parse_response(text: str) -> Dict[str, any]:
    """Parse the LLM response into a Python dictionary.

    Args:
        text: The raw response text returned by the LLM.

    Returns:
        A dictionary with keys ``qubit_update`` and ``perceived_environment``.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Fall back to an empty update and perceived environment
        return {
            "qubit_update": "",
            "perceived_environment": {
                "description": "unknown",
                "threat_level": "unknown",
                "self_state": "unknown",
            },
        }