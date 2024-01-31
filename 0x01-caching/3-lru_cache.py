#!/usr/bin/env python3
"""
LRU caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRU caching system
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Assign the item to the dictionary """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)
            while len(self.queue) >= self.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache.

        Args:
            key: The key to retrieve from the cache.

        Return:
            The value in self.cache_data linked to the key.
        """
        if key is not None and key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
