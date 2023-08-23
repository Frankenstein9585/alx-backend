#!/usr/bin/env python3
"""LIFO Cache Implementation"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache Class inherits from BaseCaching"""
    last_added = None

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the dictionary based on LIFO algorithm"""
        if key and item:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                    and key not in self.cache_data):
                print('DISCARD: {}'.format(self.last_added))
                self.cache_data.pop(self.last_added)
            self.cache_data[key] = item
            self.last_added = key

    def get(self, key):
        """Retrieves an item from the dictionary"""
        if key:
            return self.cache_data.get(key)
