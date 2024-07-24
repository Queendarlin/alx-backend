#!/usr/bin/env python3
"""
Module for MRU Caching
"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU (Most Recently Used) caching system """

    def __init__(self):
        """ Initialize the MRUCache """
        super().__init__()
        # Use OrderedDict to keep track of the order of insertions and access
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        # If the key already exists, remove it, so we can update its position
        if key in self.cache_data:
            self.cache_data.pop(key)

        # Add the key and item to the cache
        self.cache_data[key] = item

        # If the cache exceeds max size, remove the most recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the last item (most recently used) and print the key
            mru_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed item to the end to mark it as recently used
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
