#!/usr/bin/env python3
"""
Module with an annotated function processing
the length of elements stored in an iterable object.
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Description:
        Annotates the parameters and return values with the appropriate types.

    Args:
        lst (Iterable[Sequence]): an iterable object containing sequences.

    Returns:
        (List[Tuple[Sequence, int]]):
        A list of tuples where each one contains
        a sequence from `lst` and its length.
    """
    return [(i, len(i)) for i in lst]
