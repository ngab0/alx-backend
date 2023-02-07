#!/usr/bin/env python3
"""
0-simple_helper_function module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function that returns range of indexes to return in a list for
    the pagination prameters
    """
    return (0 if page == 1 else (page - 1) * page_size, page * page_size)
