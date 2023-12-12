#!/usr/bin/env python3
"""basic asyncio syntax"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """implement random delay and return it"""
    duration = random.uniform(0, max_delay)
    await asyncio.sleep(duration)
    return duration
