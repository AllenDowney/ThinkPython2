"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import math

from Wobbler import *


class Missed(Exception):
    """Exception raised when a turtle tries to tag someone too far away."""


class Tagger(Wobbler):
    """Represents a Turtle that plays tag."""

    def __init__(self, world, speed=1, clumsiness=60, color='red'):
        Wobbler.__init__(self, world, speed, clumsiness, color)
        self.it = 0
        self.sulking = 0

    def steer(self):
        """Steers the Wobbler in the general direction it should go.

        Postcondition: the Wobbler's heading may be changed, but
        its position may not.
        """
        # if sulking, decrement the sulking clock
        if self.sulking > 0:
            self.sulking -= 1
            if self.sulking == 0:
                self.color = 'red'
                self.speed = self.old_speed
            return

        # if out of bounds, turn toward the center
        if self.distance() > 200:
            self.turn_toward(0, 0)
            return

        # if not it, just wander
        if not self.it:
            return

        # if it, chase the closest player
        target = self.closest(self.world.animals)
        try:
            self.apply_tag(target)
        except Missed:
            self.chase(target)
        

    def turn_toward(self, x=0, y=0):
        """Turns to face the given point.

        x, y: point to turn toward
        """
        self.heading = self.away(x, y) + 180
        self.redraw()

    def away(self, x=0, y=0):
        """Computes the heading away from the given point.

        x, y: point to face away from
        """
        dx = self.x - x
        dy = self.y - y
        heading = math.atan2(dy, dx)
        return heading * 180 / math.pi

    def distance(self, x=0, y=0):
        """Computes the distance from this turtle to the given point.

        x, y: point to find distance to
        """
        dx = self.x - x
        dy = self.y - y
        return math.sqrt(dx**2 + dy**2)

    def distance_from(self, other):
        """Computes the distance between turtles.

        other: Turtle object
        """
        return self.distance(other.x, other.y)

    def youre_it(self):
        """Makes this turtle it."""
        self.it = 1
        self.old_speed = self.speed
        self.old_color = self.color
        self.speed = 0
        self.color = 'blue'
        self.sulking = 200
        self.redraw()

    def not_it(self):
        """Makes this turtle not it."""
        self.it = 0
        self.color = self.old_color
        self.redraw()

    def flee(self, other):
        """Faces away from the other turtle.

        other: Turtle object
        """
        self.heading = self.away(other.x, other.y)
        
    def chase(self, other):
        """Faces the other turtle.

        other: Turtle object
        """
        self.turn_toward(other.x, other.y)

    def closest(self, others):
        """Return closest animal in the list (other than self).

        others: list of Animals
        """
        t = [(self.distance_from(animal), animal)
              for animal in others if animal is not self]
        (distance, animal) = min(t)
        return animal

    def apply_tag(self, other):
        """Tried to tag the other turtle.

        If it is too far away, raises an exception.

        other: Turtle object
        """
        if self.distance_from(other) < 10:
            self.not_it()
            other.youre_it()
        else:
            raise Missed


if __name__ == '__main__':
    world = make_world(Tagger)
    world.animals[0].youre_it()
    world.mainloop()
