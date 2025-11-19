"""Concrete LLM client for OpenAI models.

This implementation shows how to integrate an OpenAI API client with the
DIT Lab simulation. The details such as API keys and endpoint URLs
should be provided via environment variables or configuration files.
"""

import os
from typing import Any

import openai  # type: ignore

from .client_base import LLMClientBase


class OpenAIClient(LLMClientBase):
    """Call OpenAI's API to obtain a response to a prompt."""

    def __init__(self, model_name: str = "gpt-3.5-turbo", **kwargs: Any) -> None:
        self.model_name = model_name
        self.api_key = os.getenv("OPENAI_API_KEY")
        # Additional parameters can be stored for later use
        self.extra_args = kwargs

    def __call__(self, prompt: str) -> str:
        """Send the prompt to the OpenAI API and return the response text."""
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY environment variable not set")
        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            **self.extra_args
        )
        # Extract the content from the first choice
        return response["choices"][0]["message"]["content"]