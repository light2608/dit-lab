"""Timeline utilities.

This module re-exports the SnapshotManager for backwards compatibility
and potential extensions. In future versions additional timeline
manipulation functions may be added here.
"""

from .state import SnapshotManager  # noqa: F401

__all__ = ["SnapshotManager"]