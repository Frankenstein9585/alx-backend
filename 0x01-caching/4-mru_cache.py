#!/usr/bin/env python3
"""MRU Cache Implementation"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRUCache Class inherits from BaseCaching"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        # ordered_dict to check the recency of entries
        self.cache = OrderedDict()

    def put(self, key, item):
        """Adds an item to the dictionary based on MRU algorithm"""
        if key and item:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                    and key not in self.cache_data):
                # last key of the ordered dict (most recent)
                most_recent_key = next(reversed(self.cache))
                print('DISCARD: {}'.format(most_recent_key))

                # remove the most recent key from both dicts
                self.cache_data.pop(most_recent_key)
                self.cache.pop(most_recent_key)
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
