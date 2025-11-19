"""Persistent storage utilities for DIT Lab.

This module provides helper functions to save and load full simulation
runs to disk. For simplicity, the current implementation uses Python's
pickle module. In a production system you might choose a more robust
format such as JSON, MessagePack or a database.
"""

import pickle
from pathlib import Path
from typing import Any, Dict


def save_run(data: Dict[str, Any], filepath: str) -> None:
    """Save run data to a file using pickle.

    Args:
        data: A dictionary containing run metadata, state snapshots, etc.
        filepath: Path to the file where data should be saved.
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as f:
        pickle.dump(data, f)


def load_run(filepath: str) -> Dict[str, Any]:
    """Load run data from a file using pickle.

    Args:
        filepath: Path to the file containing saved run data.

    Returns:
        The data dictionary loaded from the file.
    """
    path = Path(filepath)
    with path.open("rb") as f:
        return pickle.load(f)