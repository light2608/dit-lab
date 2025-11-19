"""Basic JSONL logger for DIT Lab.

This module defines a simple logger that writes each record to a new line
in a JSON file. It can be used to record simulation metrics or other
information during experiments.
"""

import json
from pathlib import Path
from typing import Any, Dict


class JSONLLogger:
    """Write records to a JSONL (JSON Lines) file."""

    def __init__(self, filepath: str) -> None:
        self.path = Path(filepath)
        # Ensure parent directory exists
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def log(self, record: Dict[str, Any]) -> None:
        """Append a single record to the log file."""
        with self.path.open("a", encoding="utf-8") as f:
            json.dump(record, f)
            f.write("\n")