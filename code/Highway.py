""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

import math
import random

from swampy.TurtleWorld import TurtleWorld, Turtle
import color_list


class Highway(TurtleWorld):
    """A circular Highway with one lane that spirals down the canvas.
    
    Attributes:

    rows: the number of rows that spiral down the canvas.
    delay: time between steps in seconds
    colors: list of RGB strings
    """
    def __init__(self):
        TurtleWorld.__init__(self)
        self.rows = 2.0
        self.delay = 0.01
        self.colors = color_list.make_color_dict().values()

    def random_color(self):
        """Returns a random RGB string in #RRGGBB format."""
        return random.choice(self.colors)

    def get_length(self):
        """Returns the total length of this highway."""
        return self.ca_width * self.rows

    def project(self, turtle):
        """Project the turtle onto the highway.

        Reads the Turtle's position position and returns its
        x,y coordinates.
        """
        p = 1.0 * turtle.position % self.get_length()
        x = p % self.ca_width
        y = p / self.ca_width * self.ca_height / self.rows
        return x, y

    def lane_heading(self):
        """Returns the heading that aligns the turtle with the lane."""
        x = self.ca_width
        y = 1.0 * self.ca_height / self.rows
        angle = math.atan2(y, x)
        heading = angle * 180 / math.pi
        return heading

    def step(self):
        """Performs one time step."""
        TurtleWorld.step(self)
        
        # compute average turtle speed
        total = 0.0
        for turtle in self.animals:
            total += turtle.speed

        print total / len(self.animals)

    def make_drivers(self, n, constructor):
        """Make drivers at random positions.

        Args:
            n: number of Drivers
            constructor: function that returns a Driver

        Returns:
            a list of Drivers.
        """
        t = []
        for i in range(n):
            turtle = constructor(self)
            t.append((turtle.position, turtle))

        # link up the drivers so each has an attribute (next) that
        # refers to the driver in front
        t.sort()
        turtles = [t[1] for t in t]
        for i in range(n-1):
            turtles[i].next = turtles[i+1]
        turtles[-1].next = turtles[0]

        return turtles


class Driver(Turtle):
    """A Turtle with a random position, speed and color."""

    def __init__(self, *args, **kwds):
        Turtle.__init__(self, *args, **kwds)
        self.delay = 0
        self.color = self.world.random_color()
        self.position = random.randrange(0, self.world.get_length())

        self.speed_limit = 4
        self.speed = random.randrange(0, self.speed_limit)
        self.safe_distance = 30

        self.heading = self.world.lane_heading()
        self.next = None
        self.project()
        self.redraw()

    def project(self):
        """Sets x and y according to position."""
        self.x, self.y = self.world.project(self)

    def accelerate(self, change):
        """Speeds up the Turtle by the given amount, within bounds."""
        self.speed += change
        if self.speed < 0:
            self.speed = 0

        if self.speed > self.speed_limit:
            self.speed = self.speed_limit

    def brake(self, change):
        """Slows down the Turtle by the given amount, within bounds."""
        self.accelerate(-change)

    def step(self):
        """Checks the distance to the next driver, adjusts speed, and moves.
        
        This function enforces the rules for all drivers.
        
        Driver decision-making is in choose_acceleration().
        """
        dist = self.find_distance()

        # get acceleration
        change = self.choose_acceleration(dist)
        self.accelerate(change)

        # if the resulting speed would cause a collision, jam on the brakes
        if self.speed > dist:
            self.speed = 0

        # move
        self.position += self.speed
        self.project()
        self.redraw()

    def find_distance(self):
        """Finds the distance between this Turtle and the next."""
        dist = self.next.position - self.position

        # deal with wrap-around
        if dist < 0:
            dist += self.world.get_length()
        return dist

    def choose_acceleration(self, dist):
        """Adjusts the speed of the Driver."""
        if dist < self.safe_distance:
            return -1
        else:
            return 0.3

    
def make_highway(n, driver=Driver):
    """Make the highway and drivers, then run the simulation.

    Args:
        n: number of Drivers
        driver: constructor
    """

    # create the highway
    world = Highway()
    world.canvas.clear_transforms()
    world.setup_run()

    # create (n) drivers
    world.make_drivers(n, driver)

    # start the simulation, then wait for user events
    print len(world.animals)
    world.run()
    world.mainloop()


def main(script, n=20):
    n = int(n)
    make_highway(n)


if __name__ == '__main__':
    import sys
    main(*sys.argv)
