"""This code is for an exercise from
Think Python: An Introduction to Software Design

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

This program requires Gui.py, which is part of
Swampy; you can download it from thinkpython.com/swampy.

"""

from swampy.Gui import Callable
from swampy.TurtleWorld import Turtle, TurtleWorld


class Threader(Turtle):
    def __init__(self, world):
        Turtle.__init__(self, world)
        self.delay = 0.005
        self.set_color('purple')

    def step():
        """Threaders don't need no stinkin' step method.

        See http://en.wikipedia.org/wiki/Stinking_badges
        """
    
    def moveto(self, x, y):
        """Teleports to the given coordinates and redraws."""
        self.x = x
        self.y = y
        self.redraw()

    def koch(self, n):
        """Draws a Koch curve with length n.

        See http://en.wikipedia.org/wiki/Koch_snowflake
        """
        if n<8:
            self.fd(n)
            return
        for angle in [-60, 120, -60, 0]:
            self.koch(n/3.0)
            self.rt(angle)

    def snowflake(self):
        """Draws a Koch snowflake."""
        for i in range(3):
            self.koch(300)
            self.rt(120)
        self.undraw()


def make_threader(world):
    """Creates a Threader and makes it draw a snowflake."""
    t = Threader(world)
    t.moveto(-150, 90)

    # TODO: modify this so it runs in a new thread
    t.snowflake()


world = TurtleWorld()
world.setup_interactive()

# add a button that calls make_threader
world.bu(text='Make Threader', command=Callable(make_threader, world))
world.mainloop()

