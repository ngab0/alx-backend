#!/usr/bin/env python3
""" Least recently used cache module """
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that implements a LRU caching system i.e.
    least recently used - discards the least recently used items first
    """
    def __init__(self):
        """
        initializes an instance of LRUCache class
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        method that adds an item in the cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print(f'DISCARD: {lru_key}')
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        method that retrieves an item from cache by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
