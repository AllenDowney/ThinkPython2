"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

"""
To use this typewriter, you have to provide a module named letters.py
that contains functions with names like draw_a, draw_b, etc.
"""

from time import sleep

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

# check if the reader has provided letters.py
try:
    from letters import *
except ImportError, e:
    message = e.args[0]
    if message.startswith('No module'):
        raise ImportError(message + 
                          '\nYou have to provide a module named letters.py')


# The following is the code for the turtle typewriter.
# it uses some features we haven't seen yet.

def teleport(t, x, y):
    """Moves the turtle to a position in absolute coordinates."""

    # This is an example of a function that breaks the layer
    # of abstraction provided by the Level 0 primitives!
    # It takes advantage of details of the implemention that
    # should probably not be considered 'public'
    t.x = x
    t.y = y
    t.redraw()


def keypress(event):
    """Handles the event when a user presses a key.

    Checks if there is a function with the right name; otherwise
    it prints an error message.
    """
    # if we're still drawing the previous letter, bail out
    if bob.busy:
        return
    else:
        bob.busy = True

    # check if the user pressed return
    if event.char in ['\n', '\r']:
        teleport(bob, -180, bob.y-size*3)
        bob.busy = False
        return
        
    # figure out which function to call, and call it
    try:
        func = eval('draw_' + event.char)
    except NameError:
        print "I don't know how to draw an", event.char
        bob.busy = False
        return

    func(bob, size)

    skip(bob, size/2)
    bob.busy = False


world = TurtleWorld()

# create and position the turtle
size = 20
bob = Turtle(world)
bob.delay = 0.01
bob.busy = False
teleport(bob, -180, 150)

# tell world to call keypress when the user presses a key
world.bind('<Key>', keypress)

world.mainloop()
