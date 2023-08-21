#!/usr/bin/env python3
"""REST API: Pagination"""
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """This function returns a tuple
    of size two containing a start index and an end index
    corresponding to the range of indexes to return in a
    list for those particular pagination parameters."""
    start_index = page * page_size - page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets records from pages based on page number and page size
        using simple pagination"""
        assert type(page) == int and type(page_size) == int
        assert page != 0 and page_size != 0
        assert page >= 0 and page_size >= 0
        start, end = index_range(page, page_size)
        if end > len(self.dataset()):
            return []
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """This is an implementation of hypermedia pagination"""
        dataset_size = len(self.dataset())
        page_length = len(self.get_page(page, page_size))
        next_page = None if page * page_size >= dataset_size else page + 1
        prev_page = None if page == 1 else page - 1
        total_pages = math.ceil(dataset_size / page_size)
        return {
            'page_size': page_length,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
