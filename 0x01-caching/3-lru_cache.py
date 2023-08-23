#!/usr/bin/env python3
"""LRU Cache Implementation"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRUCache Class inherits from BaseCaching"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        # ordered_dict to check the recency of entries
        self.cache = OrderedDict()

    def put(self, key, item):
        """Adds an item to the dictionary based on LRU algorithm"""
        if key and item:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                    and key not in self.cache_data):
                # first key of the ordered dict (least recent)
                least_recent_key = next(iter(self.cache))
                print('DISCARD: {}'.format(least_recent_key))

                # remove the least recent key from both dicts
                self.cache_data.pop(least_recent_key)
                self.cache.pop(least_recent_key)
            self.cache_data[key] = item
            self.cache[key] = item

            # move the most recent key to the end of the dict
            self.cache.move_to_end(key)

    def get(self, key):
        """Retrieves an item from the dictionary"""
        if key:
            # move key to the end only if it exists in the dict
            if key in self.cache:
                self.cache.move_to_end(key)
            return self.cache_data.get(key)
