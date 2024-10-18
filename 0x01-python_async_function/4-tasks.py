#!/usr/bin/env python3
'''This module contains asynchronous coroutine wait_n,
which spawns the wait_random function n times with a
specified max_delay. It will return the list of delays
in ascending order (without using sort()) by collecting
them as they complete.'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronously run wait_random n times and return
    list of delays in ascending order."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
