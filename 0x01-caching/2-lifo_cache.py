#!/usr/bin/env python3
""" Last-in-first-out cache module """
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that implements a LIFO caching system i.e.
    Last in first out - cache evicts the block added most recently first.
    """
    def __init__(self):
        """
        initializes the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        method that adds an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS and \
           key not in self.cache_data:
            last_key, _ = self.cache_data.popitem(True)
            print(f'DISCARD: {last_key}')
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        method that retrieves an item from cache by key
        """
        return self.cache_data.get(key, None)
