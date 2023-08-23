#!/usr/bin/env python3
"""LIFO Cache Implementation"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LIFOCache Class inherits from BaseCaching"""
    last_added = None

    def __init__(self):
        """Initialize"""
        super().__init__()
        # ordered_dict to check the recency of entries
        self.cache = OrderedDict()

    def put(self, key, item):
        """Adds an item to the dictionary based on LIFO algorithm"""
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
            print(self.cache)

    def get(self, key):
        """Retrieves an item from the dictionary"""
        if key:
            # move key to the end only if it exists in the dict
            if key in self.cache:
                self.cache.move_to_end(key)
            print(self.cache)
            return self.cache_data.get(key)


my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
