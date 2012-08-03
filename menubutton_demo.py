"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from swampy.Gui import *

g = Gui()
g.title('')
g.la('Select a color:')
colors = ['red', 'green', 'blue']
mb = g.mb(text=colors[0])

def set_color(color):
    print color
    mb.config(text=color)

for color in colors:
    g.mi(mb, text=color, command=Callable(set_color, color))

g.mainloop()
