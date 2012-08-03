"""Solution to an exercise from
Think Python: An Introduction to Software Design

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

This program requires Gui.py, which is part of
Swampy; you can download it from thinkpython.com/swampy.

"""

import os, sys
from swampy.Gui import *
import Image as PIL      # to avoid name conflict with Tkinter
import ImageTk

def show_image(filename):
    # tkpi has to be global because otherwise it gets
    # deallocated when the function ends.
    global tkpi

    image = PIL.open(filename)
    tkpi = ImageTk.PhotoImage(image)
    g.la(image=tkpi)

g = Gui()
show_image('allen.png')
g.mainloop()

