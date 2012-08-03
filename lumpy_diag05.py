#!/usr/bin/python

"""
Code for use with Think Python: An Introduction to Software Design

Copyright 2010 Allen B. Downey
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

from swampy.TurtleWorld import Turtle
import Lumpy

# create a Lumpy object and capture reference state
lumpy = Lumpy.Lumpy()
lumpy.opaque_class(Turtle)
lumpy.make_reference()

# run the test code
z = 5

bob = Turtle()

for i in range(3):
    x = i

def function(parameter):
    local = parameter + 1

    # draw the state while function is running
    lumpy.object_diagram()

variable = 3
function(variable+1)


