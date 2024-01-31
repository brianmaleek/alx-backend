#!/usr/bin/env python3
"""
- Description: class BasicCache inherits from BaseCaching and is a
caching system:
- Use self.cache_data - dictionary from the parent class BaseCaching
- This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    - Description: class BasicCache inherits from BaseCaching and is a
                    caching system
    """

    def put(self, key, item):
        """
        - Description: Must assign to the dictionary self.cache_data the item
                        value for the key key.
        - If key or item is None, this method should not do anything.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        - Description: Must return the value in self.cache_data linked to key.
        - If key is None or if the key doesn’t exist in self.cache_data,
            return None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
