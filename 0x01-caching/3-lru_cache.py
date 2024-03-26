#!/usr/bin/python3
"""Defining a class LRUCache that inherits from BaseCacheing"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Representation of LRUCache class"""

    def __init__(self):
        """Initialization of the class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Assign key and item to th3 cache system"""
        if not (key and item):
            return
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)

        if len(self.cache_data) >= self.MAX_ITEMS:
            curr = self.queue.pop(0)
            del self.cache_data[curr]
            print(f'DISCARD: {curr}')
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve item from the cache system"""
        if not (key and key in self.cache_data):
            return
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
