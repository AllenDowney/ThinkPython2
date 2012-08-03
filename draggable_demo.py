"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from swampy.Gui import *

class Draggable(Item):
    """A Canvas Item with bindings for dragging and dropping.

    Given an item, Draggable(item) creates bindings and returns
    a Draggable object with the same canvas and tag as the original.
    """
    def __init__(self, item):
        self.canvas = item.canvas
        self.tag = item.tag
        self.bind('<ButtonPress-1>', self.select)
        self.bind('<B1-Motion>', self.drag)
        self.bind('<ButtonRelease-1>', self.drop)

    # the following event handlers take an event object as a parameter

    def select(self, event):
        """Selects this item for dragging."""
        self.dragx = event.x
        self.dragy = event.y

        self.fill = self.cget('fill')
        self.config(fill='orange')
        
    def drag(self, event):
        """Move this item using the pixel coordinates in the event object."""
        # see how far we have moved
        dx = event.x - self.dragx
        dy = event.y - self.dragy

        # save the current drag coordinates
        self.dragx = event.x
        self.dragy = event.y

        # move the item 
        self.move(dx, dy)

    def drop(self, event):
        """Drops this item."""
        self.config(fill=self.fill)


# create the Gui and the Canvas
g = Gui()
ca = g.ca(width=500, height=500, bg='white')

def make_circle(event):
    """Makes a circle item at the location of a button press."""
    pos = ca.canvas_coords([event.x, event.y])
    item = ca.circle(pos, 5, fill='red')
    item = Draggable(item)

ca.bind('<ButtonPress-3>', make_circle)

def make_text(event=None):
    """Pressing Return in the Entry makes a text item."""
    text = en.get()
    item = ca.text([0,0], text)
    item = Draggable(item)


g.row([0,1])
bu = g.bu('Make text item:', make_text)
en = g.en()
en.bind('<Return>', make_text)

g.mainloop()
