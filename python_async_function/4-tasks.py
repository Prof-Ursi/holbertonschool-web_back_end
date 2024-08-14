#!/usr/bin/env python3
"""
Async function using asyncio Tasks
for concurrent execution of task_wait_random().
"""

from asyncio import gather
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Description:
        Execute the task_wait_random() coroutine concurrently
        a specified number of times with a specified "max_delay".

    Args:
        - n (int): the number of times to execute
        task_wait_random() concurrently.
        - max_delay (int): the maximum delay in seconds
        for each task_wait_random() execution.

    Returns:
        delay_chart (List[float]): a chart of all the delay lists,
        in ascending order.
    """
    delay_list = []

    for _ in range(n):
        delay_list.append(task_wait_random(max_delay))

    delay_chart = await gather(*delay_list)

    return sorted(delay_chart)
