"""basic asyncio syntax"""
import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> int:
    """implement random delay and return it"""
    duration = random.uniform(0, max_delay)
    await asyncio.sleep(duration)
    return duration
