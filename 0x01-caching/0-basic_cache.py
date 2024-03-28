#!/usr/bin/python3
""" Defining a class BasicCache that inherits from BasicCacheing
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Representation of the class BasicCache"""

    def __init__(self):
        """Initializing the class"""
        super().__init__()

    def put(self, key, item):
        """Assigning the dict
        Args:
            key: key of the item
            item: the item of the key
        """
        if not (key and item):
            return
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Returning the value of the key or
        None if key is None
        Args:
            key: key of the item
        """
        if not key or key not in self.cache_data:
            return
        if key:
            return self.cache_data.get(key, None)
