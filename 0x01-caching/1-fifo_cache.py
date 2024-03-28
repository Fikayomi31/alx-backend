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
        self.cache_data[key] = item
        # check length of the cache_data with MAX_ITEMS
        if len(self.cache_data) >= self.MAX_ITEMS:
            # iterating over the items in the self.cache_data
            diter = iter(self.cache_data.items())
            # next is used to retrieve the first item
            first_key, first_value = next(diter)
            del self.cache_data[first_key]
            print(f'DISCARD: {first_key}')

    def get(self, key):
        """Retrieve the value
        Args:
            key: key to the value
        """
        if key:
            return self.cache_data.get(key, None)
