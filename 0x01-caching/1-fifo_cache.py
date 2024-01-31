#!/usr/bin/env python3
"""
FIFO caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class inherits from BaseCaching and implements a caching system
    using the FIFO algorithm
    """

    def __init__(self):
        """
        Initialize FIFOCache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Description: Add an item to the cache (dictionary)

        Args:
            key: The key to be added to the cache.
            item: The value associated with the key.

        - If key or item is None, this method does nothing.
        - If the number of items in self.cache_data is higher than
            BaseCaching.MAX_ITEMS:
        - Discard the first item put in the cache (FIFO algorithm).
        - Print DISCARD: with the key discarded and followed by a new line.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
                del self.cache_data[delete]
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """Get an item from the cache.

        Args:
            key: The key to retrieve from the cache.

        Return:
            The value in self.cache_data linked to the key.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
