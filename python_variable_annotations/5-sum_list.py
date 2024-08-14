#!/usr/bin/env python3
""" Module with a function to sum a list of floats. """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Description:
        Sums a list of floating-point numbers.

    Args:
        input_list (List[float]): a list of floats.

    Returns:
        (float): the sum of the input list of floats.
    """
    return sum(input_list)
