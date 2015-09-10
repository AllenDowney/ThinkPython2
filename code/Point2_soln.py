"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __add__(self, other):
        """Adds a Point or tuple."""
        if isinstance(other, Point):
            return self.add_point(other)
        elif isinstance(other, tuple):
            return self.add_tuple(other)
        else:
            msg = "Point doesn't know how to add type " + type(other)
            raise TypeError(msg)

    def add_point(self, other):
        """Adds a point."""
        return Point(self.x + other.x, self.y + other.y)

    def add_tuple(self, other):
        """Adds a tuple."""
        return Point(self.x + other[0], self.y + other[1])



def main():
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    print(p1)
    print(p2)
    print(p1 + p2)
    print(p1 + (3, 4))

if __name__ == '__main__':
    main()

