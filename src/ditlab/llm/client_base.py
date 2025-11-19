"""Abstract base class for LLM clients.

LLM clients should implement the ``__call__`` method to accept a prompt
string and return a model response string. Concrete implementations
may require authentication and additional configuration parameters.
"""

from abc import ABC, abstractmethod


class LLMClientBase(ABC):
    """Abstract base class for any large language model client."""

    @abstractmethod
    def __call__(self, prompt: str) -> str:
        """Send the prompt to the model and return the response.

        Args:
            prompt: The prompt text to send to the model.

        Returns:
            The raw model response as a string.
        """
        raise NotImplementedError