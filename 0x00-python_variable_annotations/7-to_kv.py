#!/usr/bin/env python3
from typing import Union, Tuple
"""Take string and int/float and return tuple"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Take string and int/float and return tuple"""
    return (k, v ** 2)
