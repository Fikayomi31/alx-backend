#!/usr/bin/python3
""" LFU Caching Algorithm """
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""

    def __init__(self):
        """Class initialization"""
        super().__init__()
        # Keep track of the frequency of each key.
        self.freq = {}
    def put(self, key, item):
        """Assigning to the dictionary
        Args:
            key: key to the item
            item: value to the key
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # finding the least frequency
                min_freq = min(self.freq.values())
                # if there are more than one min_freq we will
                # check for the least value of the min_freq.key
                least_freq_keys = [
                    k for k, v in self.freq.items() if v == min_freq
                ]
                lfu_key = min(least_freq_keys, key=self.freq.get)
                # deleting it from both the cache_data and freq
                self.cache_data.pop(lfu_key)
                self.freq.pop(lfu_key)
                print("DISCARD:", lfu_key)
            # adding the new key
            self.cache_data[key] = item
            self.freq[key] = 1

    def get(self, key):
        """doc doc doc"""
        if key in self.cache_data:
            self.freq[key] += 1
            return self.cache_data.get(key)