#!/usr/bin/env python3
""" Module with an annoted function to create a multiplier function. """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Description:
        Creates a multiplier function.

    Args:
        multiplier (float): the multiplier value.

    Returns:
        Callable[[float], float]:
        A function multiplying a float by the specified multiplier.
    """
    return lambda x: x * multiplier
