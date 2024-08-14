#!/usr/bin/env python3
"""
Module with a type-annotated function converting a string
and either an int or a floating point number to a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Description:
        Converts a string and the square of an int OR a float to a tuple.

    Args:
        - k (str): the input string.
        - v (Union[int, float]): the input integer or float.

    Returns:
        (Tuple[str, float]):
        A tuple containing the string k and the square of v as a float.
    """
    return (k, v ** 2)
