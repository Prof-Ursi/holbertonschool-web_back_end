#!/usr/bin/env python3
"""
Module with an asynchronous coroutine waiting for a random delay.
"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    Description:
        Asynchronously sleeps for a random duration between 0 and max_delay.

    Args:
        max_delay (int): the maximum delay in seconds set by default at 10.

    Returns:
        random_delay (float): the actual random delay that occurred.
    """
    random_delay = uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
