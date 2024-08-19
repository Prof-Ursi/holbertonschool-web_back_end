#!/usr/bin/env python3
""" Module to measure the runtime of async_comprehension module. """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Description:
    ------------
        Measure the runtime of previously created coroutine.

    Returns:
    --------
    float
        Total runtime in seconds.
    """
    start_time = time()
    async_list = [async_comprehension() for _ in range(4)]
    await gather(*async_list)
    end_time = time()
    return (end_time - start_time)
