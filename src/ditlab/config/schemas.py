"""Configuration schemas for DIT Lab.

This module defines pydantic models for configuration files used by the
simulation laboratory. These configurations include parameters for the
environment, brain, LLM settings, and lab controller.
"""

from typing import Any, Dict

from pydantic import BaseModel, Field


class EnvironmentConfig(BaseModel):
    """Configuration for the environment."""

    env_type: str = Field(
        "simple_1d",
        description="Identifier for the environment implementation to use.",
    )
    size: int = Field(
        10,
        description="The size of the 1D environment (number of discrete positions).",
    )


class BrainConfig(BaseModel):
    """Configuration for the brain/cognitive engine."""

    num_qubits: int = Field(
        4,
        description="Number of qubits (superposition states) in the brain.",
    )


class LLMConfig(BaseModel):
    """Configuration for the LLM client."""

    model_name: str = Field(
        "gpt-3.5-turbo",
        description="The identifier of the LLM model to use.",
    )
    temperature: float = Field(
        0.7,
        ge=0.0,
        le=1.0,
        description="Sampling temperature for the LLM.",
    )
    additional_settings: Dict[str, Any] = Field(
        default_factory=dict,
        description="Any additional parameters passed to the LLM client.",
    )


class LabConfig(BaseModel):
    """Top-level configuration for an experiment."""

    environment: EnvironmentConfig = Field(
        default_factory=EnvironmentConfig,
        description="Environment configuration settings.",
    )
    brain: BrainConfig = Field(
        default_factory=BrainConfig,
        description="Brain configuration settings.",
    )
    llm: LLMConfig = Field(
        default_factory=LLMConfig,
        description="LLM client configuration settings.",
    )
