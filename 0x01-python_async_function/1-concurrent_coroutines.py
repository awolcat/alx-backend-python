#!/usr/bin/env python3
"""concurrent execution"""
import asyncio
from typing import List
from heapq import nsmallest
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """concurrent execution"""
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return nsmallest(n, delays)
