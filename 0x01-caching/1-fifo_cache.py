#!/usr/bin/env python3
"""FIFO Cache Implementation"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache Class inherits from BaseCaching"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the dictionary"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print('DISCARD: {}'.format(next(iter(self.cache_data))))
                self.cache_data.pop(next(iter(self.cache_data)))

    def get(self, key):
        """Retrieves an item from the dictionary"""
        if key:
            return self.cache_data.get(key)
