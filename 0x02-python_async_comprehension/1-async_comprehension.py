#!/usr/bin/env python3
'''This module contains the async_comprehension coroutine
that collects 10 random numbers from async_generator.'''
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers asynchronously
    from async_generator."""
    return [num async for num in async_generator()]
