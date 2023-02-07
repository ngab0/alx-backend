#!/usr/bin/env python3
""" Basic cache module """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that implements a caching system
    """
    def __init__(self):
        """
        initializes an instance of BasicCache class
        """
        super().__init__()

    def put(self, key, item):
        """
        method that assigns to dictionary self.cache_data the item value
        for the key key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        method that returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
