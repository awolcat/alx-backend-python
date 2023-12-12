#!/usr/bin/env python3
import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random
"""returns a asyncio.Task instance"""


def task_wait_random(max_delay: int) -> Task:
    """returns a asyncio.Task instance"""
    return asyncio.create_task(wait_random(max_delay))
