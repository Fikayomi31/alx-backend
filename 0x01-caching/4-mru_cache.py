#!/usr/bin/python3
"""Defining a class that inherits from BaseCaching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Representation of the class"""

    def __init__(self):
        """Initialization of the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assigning to the dictionary
        Args:
            key: key to the item
            item: value to the key
        """
        if not (key and item):
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            remove = self.order.pop()
            del self.cache_data[remove]
            print(f'DISCARD: {remove}')
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve item from the cache system"""
        if key in self.cache_data:
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
