"""UI subpackage for DIT Lab.

This subpackage contains user interfaces for interacting with the
simulation. At present it provides a command-line interface. A textual
UI (based on the Textual framework) is planned for a later stage of
development.
"""

from .cli import run_cli  # noqa: F401

__all__ = ["run_cli"]