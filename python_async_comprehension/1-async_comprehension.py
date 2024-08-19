#!/usr/bin/env python3
""" Module with asynchronous generators and comprehension. """

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Description:
    ------------
        Generates a list of floats asynchronously.

    Returns:
    --------
    List[float]
        List of floats generated asynchronously.
    """
    return [n async for n in async_generator()]
