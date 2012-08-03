"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from swampy.Gui import *

g = Gui()
g.title('')

def callback1():
    g.bu(text='Now press me.', command=callback2)

def callback2():
    g.la(text='Nice job.')

g.bu(text='Press me.', command=callback1)

g.mainloop()
