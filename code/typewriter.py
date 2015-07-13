"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import string
import turtle

"""
To use this typewriter, you have to provide a module named letters.py
that contains functions with names like draw_a, draw_b, etc.
"""

# check if the reader has provided letters.py
try:
    import letters
except ImportError as e:
    message = e.args[0]
    if message.startswith('No module'):
        raise ImportError(message + 
                          '\nYou have to provide a module named letters.py')


def teleport(t, x, y):
    """Moves the turtle without drawing a line.

    Postcondition: pen is down

    t: Turtle
    x: coordinate
    y: coordinate
    """
    t.pu()
    t.goto(x, y)
    t.pd()


def keypress(char):
    """Handles the event when a user presses a key.

    Checks if there is a function with the right name; otherwise
    it prints an error message.

    char: string, letter to draw
    """
    # if we're still drawing the previous letter, bail out
    if bob.busy:
        return
    else:
        bob.busy = True

    # figure out which function to call, and call it
    try:
        name = 'draw_' + char
        func = getattr(letters, name)
    except AttributeError:
        print("I don't know how to draw an", char)
        bob.busy = False
        return

    func(bob, size)

    letters.skip(bob, size/2)
    bob.busy = False


def carriage_return():
    """Moves to the beginning of the next line.
    """
    teleport(bob, -180, bob.ycor() - size*3)
    bob.busy = False


def presser(char):
    """Returns a function object that executes keypress.

    char: character to draw when the function is executed

    returns: function with no arguments
    """
    def func():
        keypress(char)
    return func


# create and position the turtle
size = 20
bob = turtle.Turtle()
bob.busy = False
teleport(bob, -180, 150)

# tell world to call keypress when the user presses a key
screen = bob.getscreen()

for char in string.ascii_lowercase:
    screen.onkey(presser(char), char)

screen.onkey(carriage_return, 'Return')

screen.listen()
turtle.mainloop()
