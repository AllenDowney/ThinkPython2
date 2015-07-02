"""This module is part of Swampy, a suite of programs available from
allendowney.com/swampy.

Copyright 2010 Allen B. Downey
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

# import everything from the random module
from random import *

# import everything from TurtleWorld
try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


# a Wanderer is a kind of turtle
class Wanderer(Turtle):

    def __init__(self, speed=1, clumsiness=60):
        """Initializes a Wanderer.

        This is the function that creates new turtles.
        the first parameter is the new turtle itself,
        which is provided automatically when we invoke
        Wanderer()

        """
        # first, make a Turtle
        Turtle.__init__(self)

        # then add the other attributes that make it a Wanderer
        self.delay = 0

        # speed is the distance the Wanderer moves per step
        self.speed = speed

        # clumsiness determines the ability of the Wanderer to
        # track a straight line
        self.clumsiness = clumsiness

        # Wanderers start out facing in a random direction
        self.rt(randint(0,360))

    def distance(self):
        """Computes the distance from the Turtle to the origin."""

        # change the following line to compute distance correctly
        return self.get_x() + self.get_y()

    def step(self):
        """Invoked whenever the turtle is supposed to move."""

        # you are not allowed to modify this method

        # here is how to invoke a method on a Wanderer
        dist = self.distance()

        # call the function that keeps the Wanderers in bounds
        self.keep_in_bounds(dist)
        
        # choose a random direction and turn
        dir = randint(0,self.clumsiness) - randint(0,self.clumsiness)
        self.rt(dir)
        
        # move forward according to the speed attribute
        self.fd(self.speed)

    def keep_in_bounds(self, dist):
        """Turns the Turtle in order to keep it in bounds."""

        # you should modify this method
        pass
        

# create a new TurtleWorld
world = TurtleWorld()

# add the Run, Stop, Step and Clear buttons
world.setup_run()

# make three Wanderers with different speed and clumsiness attributes
for i in range(1,4):
    Wanderer(i, i*45)

# tell world to start processing events (button presses, etc)
wait_for_user()

