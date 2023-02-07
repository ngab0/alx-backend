#!/usr/bin/env python3
""" Most recently used cache module """
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that implements a MRU caching system i.e.
    most recently used - discards most recently used items first
    """
    def __init__(self):
        """
        initializes an instance of MRUCache class
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        method that adds an item to the cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print(f'DISCARD: {mru_key}')
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        method that retrieves item from cache by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
