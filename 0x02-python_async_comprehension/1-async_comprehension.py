#!/usr/bin/env python3
"""async generator"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return 10 random numbers generated asynchronously in task 0"""
    results = [i async for i in async_generator()]
    return results