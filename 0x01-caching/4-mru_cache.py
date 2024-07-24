#!/usr/bin/env python3
""" MRUCache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache defines a Most Recently Used caching system.
    """

    def __init__(self):
        """
        Initialize the MRUCache with the parent's init method
        and set up order tracking.
        """
        super().__init__()
        self.order = []  # List to track the order of usage for MRU

    def put(self, key, item):
        """
        Cache a key-value pair.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                # Discard the most recently used item
                # The most recently used key is at the end of the list
                mru_key = self.order[-1]
                del self.cache_data[mru_key]  # Remove from cache
                self.order.remove(mru_key)  # Remove from order tracking
                print(f"DISCARD: {mru_key}")

        if key in self.cache_data:
            # Remove the key from its previous position
            self.order.remove(key)
        self.cache_data[key] = item  # Add or update the cache
        # Add the key to the end to mark it as most recently used
        self.order.append(key)

    def get(self, key):
        """
        Return the value linked to the given key, or None.
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the order list
        # to mark it as most recently used
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
