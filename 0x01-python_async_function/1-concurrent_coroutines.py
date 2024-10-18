#!/usr/bin/env python3
'''This module contains asynchronous coroutine wait_n,
which spawns the wait_random function n times with a
specified max_delay. It will return the list of delays
in ascending order (without using sort()) by collecting
them as they complete.'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronously run wait_random n times and return
    list of delays in ascending order."""
    delays = []

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays