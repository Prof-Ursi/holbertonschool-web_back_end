#!/usr/bin/env python3
""" Module with a function that returns a Task """

from asyncio import create_task, Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Description:
        Create an asyncio Task to execute wait_random()
        with a specified max_delay.

    Args:
        max_delay (int): the maximum delay in seconds for wait_random().

    Returns:
        (Task): an asyncio Task object representing
        the execution of wait_random().
    """
    return create_task(wait_random(max_delay))
