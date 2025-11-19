"""Configuration package.

This subpackage contains models and helpers for loading and validating
configuration files for experiments. The actual schemas are defined in
`schemas.py`.
"""

from .schemas import LabConfig  # noqa: F401

__all__ = ["LabConfig"]