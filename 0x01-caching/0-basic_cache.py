#!/usr/bin/env python3
"""BasicCache Class"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache Class inherits from BaseCaching"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the dictionary"""
        if key:
            return self.cache_data.get(key)
