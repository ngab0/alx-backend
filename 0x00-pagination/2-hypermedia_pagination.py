#!/usr/bin/env python3
"""
2-hypermedia_pagination module
"""
import csv
import math
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        initilize an instance of Server class
        """
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
        function that returns the appropriate page of the dataset
        """
        assert(type(page) is int and page > 0)
        assert(type(page_size) is int and page_size > 0)
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        try:
            data = dataset[start:end]
        except IndexError:
            data = []
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """"
        method that returns dictionary containing:- page_size, page, data,
        next_page, prev_page, total_pages
        """
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        data = self.get_page(page, page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page + 1 < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
