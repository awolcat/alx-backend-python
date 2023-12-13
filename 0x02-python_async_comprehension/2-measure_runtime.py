#!/usr/bin/env python3
"""Measure total runtime"""


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime to generate 4 lists of len 10"""
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = time.time()
    return end_time - start_time
