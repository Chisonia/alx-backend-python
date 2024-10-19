#!/usr/bin/env python3
'''This module contains the async_generator coroutine
that yields random numbers asynchronously.'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """Asynchronously generate 10 random numbers
    between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
