"""Top‑level package for DIT Lab.

This package exposes the major modules of the project, such as the environment,
brain, lab controller, and LLM interfaces. It is intentionally lightweight;
subpackages contain the bulk of the implementation.
"""

__all__ = [
    "env",
    "brain",
    "lab",
    "llm",
    "graphmodel",
    "io",
    "util",
]