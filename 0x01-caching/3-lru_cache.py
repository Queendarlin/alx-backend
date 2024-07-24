#!/usr/bin/env python3
"""
Module for LRU Caching
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching system """

    def __init__(self):
        """ Initialize the LRUCache """
        super().__init__()
        # Use an OrderedDict to keep track of the order of insertions
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

        # If the cache exceeds max size, remove the least recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the first item (least recently used) and print the key
            lru_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed item to the end to mark it as recently used
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
