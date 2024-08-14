#!/usr/bin/env python3
""" Module with a function for concurrent execution of wait_random. """

import asyncio
import typing

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Description:
        Executes the "wait_random" coroutine concurrently
        a specified number of times with a specified "max_delay".

    Args:
        - n (int): the number of times to execute wait_random concurrently.
        - max_delay (int): the maximum delay in seconds
        for each "wait_random" execution.

    Returns:
        delay_chart (List[float]): a chart of all the delay lists,
        in ascending order.
    """
    delay_list = []

    for _ in range(n):
        delay_list.append(wait_random(max_delay))

    delay_chart = await asyncio.gather(*delay_list)

    return sorted(delay_chart)
