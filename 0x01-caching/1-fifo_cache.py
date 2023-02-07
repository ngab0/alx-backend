#!/usr/bin/env python3
""" First-in-first-out cache module """
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that implements a FIFO caching system i.e.
    First in first out - cache evicts the blocks in the order they were added.
    """
    def __init__(self):
        """
        initializes the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        method that adds an item to the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print(f'DISCARD: {first_key}')

    def get(self, key):
        """
        method that retrives an item from cache by the key
        """
        return self.cache_data.get(key, None)
