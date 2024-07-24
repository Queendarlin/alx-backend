#!/usr/bin/env python3
"""Module for LFU Caching"""

from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU (Least Frequently Used) caching system """

    def __init__(self):
        """ Initialize the LFUCache """
        super().__init__()
        self.cache_data = {}
        self.freq = defaultdict(int)  # Frequency of access for each key
        self.order = defaultdict(OrderedDict)

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If the key is already in cache, update its value and frequency
            self.cache_data[key] = item
            self.freq[key] += 1
            self.order[self.freq[key]][key] = item
            self.order[self.freq[key] - 1].pop(key, None)
        else:
            # If the cache is full, discard the LFU item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used frequency
                min_freq = min(self.freq.values())
                # Find the least recently used item in this frequency
                lru_key, _ = self.order[min_freq].popitem(last=False)
                # Remove this key from the cache and frequency dictionary
                self.cache_data.pop(lru_key)
                self.freq.pop(lru_key)
                print(f"DISCARD: {lru_key}")

            # Add the new key and item
            self.cache_data[key] = item
            self.freq[key] = 1
            self.order[1][key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency of the accessed key
        self.freq[key] += 1
        # Move the key to the new frequency order
        self.order[self.freq[key]][key] = self.cache_data[key]
        # Remove the key from the previous frequency order
        self.order[self.freq[key] - 1].pop(key, None)

        return self.cache_data[key]
