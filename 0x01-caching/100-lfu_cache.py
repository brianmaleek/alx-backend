#!/usr/bin/env python3
"""
LFU caching
"""
from collections import defaultdict

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class inherits from BaseCaching and implements LFU caching
    system.
    """

    def __init__(self):
        """
        Initialize LFUCache.
        """
        super().__init__()
        self.queue = []
        self.count = defaultdict(int)  # Default value for new keys is 0

    def put(self, key, item):
        """
        Assign the item to the dictionary
        """
        if key is None or item is None:
            return

        if len(self.queue) >= self.MAX_ITEMS and key not in self.cache_data:
            discard_key = self.queue.pop(0)
            self.count.pop(discard_key)
            self.cache_data.pop(discard_key)
            print(f"DISCARD: {discard_key}")

        if key in self.cache_data:
            self.queue.remove(key)
            self.count[key] += 1
        else:
            self.count[key] = 0

        insert_index = 0
        while insert_index < len(self.queue) and \
                not self.count[self.queue[insert_index]]:
            insert_index += 1

        self.queue.insert(insert_index, key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache.

        Args:
            key: The key to retrieve from the cache.

        Returns:
            The value associated with the given key.
        """
        if key in self.cache_data:
            self.count[key] += 1
            while (self.queue.index(key) + 1 < len(self.queue) and
                   self.count[key] >= self.count
                    [self.queue[self.queue.index(key) + 1]]):
                self.queue.insert(self.queue.index(key) + 1,
                                  self.queue.pop(self.queue.index(key)))

            return self.cache_data[key]

        return None
