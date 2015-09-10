"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


class LinearMap:
    """A simple implementation of a map using a list of tuples
    where each tuple is a key-value pair."""

    def __init__(self):
        self.items = []

    def add(self, k, v):
        """Adds a new item that maps from key (k) to value (v).
        Assumes that they keys are unique."""
        self.items.append((k, v))

    def get(self, k):
        """Looks up the key (k) and returns the corresponding value,
        or raises KeyError if the key is not found."""
        for key, val in self.items:
            if key == k:
                return val
        raise KeyError


class BetterMap:
    """A faster implementation of a map using a list of LinearMaps
    and the built-in function hash() to determine which LinearMap
    to put each key into."""

    def __init__(self, n=100):
        """Appends (n) LinearMaps onto (self)."""
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())

    def find_map(self, k):
        """Finds the right LinearMap for key (k)."""
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self, k, v):
        """Adds a new item to the appropriate LinearMap for key (k)."""
        m = self.find_map(k)
        m.add(k, v)

    def get(self, k):
        """Finds the right LinearMap for key (k) and looks up (k) in it."""
        m = self.find_map(k)
        return m.get(k)


class HashMap:
    """An implementation of a hashtable using a BetterMap
    that grows so that the number of items never exceeds the number
    of LinearMaps.

    The amortized cost of add should be O(1) provided that the
    implementation of sum in resize is linear."""

    def __init__(self):
        """Starts with 2 LinearMaps and 0 items."""
        self.maps = BetterMap(2)
        self.num = 0

    def get(self, k):
        """Looks up the key (k) and returns the corresponding value,
        or raises KeyError if the key is not found."""
        return self.maps.get(k)

    def add(self, k, v):
        """Resize the map if necessary and adds the new item."""
        if self.num == len(self.maps.maps):
            self.resize()

        self.maps.add(k, v)
        self.num += 1

    def resize(self):
        """Makes a new map, twice as big, and rehashes the items."""
        new_map = BetterMap(self.num * 2)

        for m in self.maps.maps:
            for k, v in m.items:
                new_map.add(k, v)

        self.maps = new_map


def main():
    import string

    m = HashMap()
    s = string.ascii_lowercase

    for k, v in enumerate(s):
        m.add(k, v)

    for k in range(len(s)):
        print(k, m.get(k))


if __name__ == '__main__':
    main()
