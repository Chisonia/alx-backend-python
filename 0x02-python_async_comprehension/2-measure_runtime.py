#!/usr/bin/env python3
'''This module contains the measure_runtime coroutine
that executes async_comprehension four times in parallel
and measures the total runtime.'''

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime for executing
    async_comprehension four times in parallel."""
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    stop_time = time.time()

    total_time = stop_time - start_time

    return total_time
