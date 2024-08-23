#!/usr/bin/env python3
"""
Module with a function taking two integer arguments,
and returning a tuple of size two containing a start index and an end index.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Description:
    ------------
        Returns a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.

    Args :
    ------
    page (int):
        Current page number, 1-indexed.
    page_size (int):
        Number of items per page

    Returns:
    --------
    (tuple):
        A tuple containing the start index and end index
        for the given pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
