#!/usr/bin/env python3
from typing import Callable
"""Take a float and return a function with a multiplier var in itsnamespace"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Take a float and return a fn with a multiplier var in namespace"""
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
