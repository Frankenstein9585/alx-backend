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
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """This is an implementation of deletion in hypermedia pagination
        using indexes"""
        assert 0 <= index < len(self.indexed_dataset())
        # dataset = [self.indexed_dataset().get(idx)
        # for idx in range(index, index + page_size)]
        dataset = []
        begin = index
        end = index + page_size
        # for idx in range(begin, end):
        #     if not self.indexed_dataset().get(idx):
        #         end += 1
        #     if idx in self.indexed_dataset():
        #         dataset.append(self.indexed_dataset()[idx])

        while len(dataset) != page_size:
            if not self.indexed_dataset().get(begin):
                end += 1
            else:
                dataset.append(self.indexed_dataset().get(begin))
            begin += 1
        next_index = end
        return {
            'index': index,
            'data': dataset,
            'page_size': len(dataset),
            'next_index': next_index
        }
