#!/usr/bin/env python3
"""
Function that two 2 integer argument
"""


def index_range(page, page_size):
    """
    Return tuple of size twobcontaining a start index
    and an end index
    """
    start_index = (page - 1) * page_size
    end_index = (page * page_size)
    return (start_page, end_page)
