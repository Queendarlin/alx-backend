#!/usr/bin/env python3
"""Module for LIFO Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        # If the key is already in the cache, remove it from the order list
        if key in self.cache_data:
            self.order.remove(key)

        # Add the key to the cache and the order list
        self.cache_data[key] = item
        self.order.append(key)

        # If the cache exceeds the max size, remove the last item (LIFO)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.order.pop(-2)  # Remove the second last added key
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
