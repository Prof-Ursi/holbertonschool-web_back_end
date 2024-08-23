#!/usr/bin/env python3
"""
Module containing a server class to paginate a database of popular baby names.
"""

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Description:
        ------------
            Takes two pagination parameters as arguments and returns
            the corresponding page of the dataset based on
            the specified pagination parameters.

        Args:
        -----
        page (int):
            Current page number, 1-indexed and default value set at 1.
        page_size (int):
            Number of items per page, default set at 10.

        Returns:
        --------
        (list[list]):
            A list containing the data following the specified
            pagination parameters.
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        page_indexes: tuple = index_range(page, page_size)
        dataset: List = self.dataset()

        current_page_data = dataset[page_indexes[0]:page_indexes[1]]
        return current_page_data
