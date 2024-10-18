#!/usr/bin/env python3
'''This module contains a function wait_random that
generates a random delay using random.uniform(0, max_delay)
to get a float value between 0 and max_delay.
It uses await asyncio.sleep(delay) to asynchronously wait
for the generated delay time.
Finally, it returns the delay.'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random
    delay and returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
