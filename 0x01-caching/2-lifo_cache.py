#!/isr/bin/python3
"""Defining a class LIFOCache that inherits from BaseCaching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Representation of class LIFoCache"""

    def __init__(self):
        """Initilization of the class"""
        super().__init__()
        self.stack = []

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
        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.stack:
            # Getting the last item
            last_key = self.stack.pop()
            del self.cache_data[last_key]
            print(f'DISCARD: {last_key}')
        if key and item:
            # appending inside stack to keep track of last item
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value
        Args:
            key: key to the value
        """
        if key:
            return self.cache_data.get(key, None)
