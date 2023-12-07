#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
"""Sequence"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """sequences"""
    return [(i, len(i)) for i in lst]
