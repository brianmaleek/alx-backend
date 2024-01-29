#!/usr/bin/env python3
"""
- Description: function named index_range takes two integer arguments page and
                page_size.

- Return: The function returns a tuple of size two containing a start index
            and an end index corresponding to the range of indexes to return
            in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page and page size.

    Args:
    - page (int): The page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple: A tuple containing the start and end indexes for the specified
    page.
    """
    if page < 1 or page_size < 1:
        raise ValueError("Both page and page_size should be positive integers")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
