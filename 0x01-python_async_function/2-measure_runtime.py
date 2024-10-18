#!/usr/bin/env python3
'''This module contains a function with integers n and max_delay
as arguments that measures the total execution time
for wait_n(n, max_delay), and returns total_time / n,
which is a float.'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the average runtime of wait_n over n executions."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time = time.time()
    average_time = (stop_time - start_time) / n
    return average_time
