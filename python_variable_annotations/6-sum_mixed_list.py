#!/usr/bin/env python3
"""
Module with a function to sum a mixed list
comprised of integers and floating point numbers.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Description:
        Sums a mixed list containing integer and/or float numbers.

    Args:
        mxd_lst (List[Union[int, float]]):
        A list containing either integers and/or floats.

    Returns:
        (float): the sum of the input list elements.
    """
    return sum(mxd_lst)
