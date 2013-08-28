"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from swampy.Gui import *
from Tkinter import PhotoImage

g = Gui()
photo = PhotoImage(file='danger.gif')
g.bu(image=photo)

canvas = g.ca(width=300)
canvas.image([0,0], image=photo)

import Image as PIL
import ImageTk

image = PIL.open('allen.png')
photo2 = ImageTk.PhotoImage(image)
g.la(image=photo2)

g.mainloop()
