"""LLM integration subpackage.

This package defines abstract interfaces for connecting to large language
models and concrete implementations for specific providers. It also
contains helper functions for constructing prompts.
"""

from .client_base import LLMClientBase  # noqa: F401
from .openai_client import OpenAIClient  # noqa: F401
from .prompts import build_prompt  # noqa: F401

__all__ = ["LLMClientBase", "OpenAIClient", "build_prompt"]