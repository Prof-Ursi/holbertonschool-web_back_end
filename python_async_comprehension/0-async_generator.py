#!/usr/bin/env python3
""" Module containing an async generator coroutine. """

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Description:
    ------------
        Generates 10 random numbers asynchronously.

    Yields:
    -------
    float
        Random number between 0 and 10.
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
