"""Random seed utilities.

This module provides a simple helper to set the random seed for both
NumPy and Python's built-in random module. It is useful for reproducible
experiments.
"""

import random
import numpy as np


def set_random_seed(seed: int) -> None:
    """Set the random seed for NumPy and random.

    Args:
        seed: The seed value to use.
    """
    random.seed(seed)
    np.random.seed(seed)