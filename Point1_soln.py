"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import copy
import math

# to avoid duplicating code, I'm importing everything from Point1 
from Point1 import *


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects."""
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist


def move_rectangle(rect, dx, dy):
    """Move the Rectangle by modifying its corner object.

    rect: Rectangle object.
    dx: change in x coordinate (can be negative).
    dy: change in y coordinate (can be negative).
    """
    rect.corner.x += dx
    rect.corner.y += dy


def move_rectangle_copy(rect, dx, dy):
    """Move the Rectangle and return a new Rectangle object.

    rect: Rectangle object.
    dx: change in x coordinate (can be negative).
    dy: change in y coordinate (can be negative).
    """
    new = copy.deepcopy(rect)
    move_rectangle(new, dx, dy)
    return new


def main():
    blank = Point()
    blank.x = 0
    blank.y = 0

    grosse = Point()
    grosse.x = 3
    grosse.y = 4

    print 'distance',
    print distance_between_points(grosse, blank)


    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print box.corner.x
    print box.corner.y
    print 'move'
    move_rectangle(box, 50, 100)
    print box.corner.x
    print box.corner.y

    new_box = move_rectangle_copy(box, 50, 100)
    print box.corner.x
    print box.corner.y

if __name__ == '__main__':
    main()

