"""Code for use with Think Python by Allen Downey.

Copyright 2010 Allen B. Downey
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

import math


class Location(object):
    """Represents a point in 2-D space."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        """Computes the distance from this location to other."""
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)

    def isLeft(self, other): return self.x < other.x
    def isRight(self, other): return self.x > other.x
    def isAbove(self, other): return self.y > other.y
    def isBelow(self, other): return self.y < other.y


class Shape(object):
    """The parent class that all shapes inherit from."""


class Circle(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def contains(self, loc):
        """Returns True if Location loc is inside this circle
        (including the boundary)."""       
        return loc.distance(self.center) <= self.radius


class Rectangle(Shape):
    def __init__(self, topLeft, botRight):
        self.topLeft = topLeft
        self.botRight = botRight

    def contains(self, loc):
        """return True if Location loc is inside this rectangle
        (including the boundary)"""
        if loc.isLeft(self.topLeft): return False
        if loc.isRight(self.botRight): return False
        if loc.isAbove(self.topLeft): return False
        if loc.isBelow(self.botRight): return False
        return True


center = Location(100, 200)
circle = Circle(center, 75)
loc = Location(150, 150)

bool = circle.contains(loc) 
print bool
