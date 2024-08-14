#!/usr/bin/env python3
"""
Module with a function measuring the average
execution time of the "wait_n()" routine.
"""

from asyncio import run
from time import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Description:
        Measure the total execution time for "wait_n(n, max_delay)"
        and return the average execution time by dividing
        the total execution time by n.

    Args:
        - n (int): the number of times to execute "wait_n()" concurrently.
        - max_delay (int): the maximum delay in seconds for
        each "wait_n()" execution.

    Returns:
        (float): the average execution time per "wait_n()" call.
    """
    start_time = time()
    run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time

    return float(total_time / n)
