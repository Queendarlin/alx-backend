#!/usr/bin/env python3
"""
Module for MRU Caching
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU (Most Recently Used) caching system """

    def __init__(self):
        """ Initialize the MRUCache """
        super().__init__()
        self.cache_data = {}  # Dictionary to store cache data
        self.order = []  # List to maintain the order of access

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        # If the key is already in the cache
        # update its value and move it to the end
        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
        else:
            # Add the new item to the cache
            self.cache_data[key] = item
            self.order.append(key)

        # If the cache exceeds the maximum number of items
        # discard the most recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # The most recently used item is the last one in the order list
            most_recent_key = self.order.pop(-1)
            del self.cache_data[most_recent_key]
            print(f"DISCARD: {most_recent_key}")

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end
        # to mark it as the most recently used
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
