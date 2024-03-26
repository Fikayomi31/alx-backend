#!/isr/bin/python3
"""Defining a class FIFOCache that inherits from BaseCaching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Representation of class FIFoCache"""

    def __init__(self):
        """Initilization of the class"""
        super().__init__()

    def put(self, key, item):
         """Caches a new item and makes sure
         that it doesn't exceed the limit
         Args:
             key: the key of the item
             item: the item to be cached
         """
         if not (key and item):
             return
         