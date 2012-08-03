"""Solution to an exercise from
Think Python: An Introduction to Software Design

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

This program requires Gui.py, which is part of
Swampy; you can download it from thinkpython.com/swampy.

"""

from swampy.Gui import *

def figure1():
    print 'Figure 17.3 a'

    g = Gui()
    b1 = g.bu(text='OK', command=g.quit)
    b2 = g.bu(text='Cancel')
    b3 = g.bu(text='Help')

    g.mainloop()


def figure2():
    print 'Figure 17.3 b'

    b2.configure(text='Cancel Command')

    g.mainloop()

def figure3():
    print 'Figure 17.3 c'

    for b in [b1, b2, b3]:
        b.pack(side=TOP)

    g.mainloop()
    g.destroy()


def figure4():
    print 'Figure 17.4 a'

    g = Gui()
    options = dict(side=LEFT, padx=10, pady=10)
    b1 = g.bu(text='OK', command=g.quit, **options)
    b2 = g.bu(text='Cancel', **options)
    b3 = g.bu(text='Help', **options)

    g.mainloop()


def figure5():
    print 'Figure 17.4 b'

    options = dict(side=LEFT, padx=0, pady=0, ipadx=10, ipady=10)
    for b in [b1, b2, b3]:
        b.pack(**options)

    g.mainloop()


def figure6():
    print 'Figure 17.4 c'

    options = dict(side=LEFT, padx=10, pady=10, ipadx=10, ipady=10)
    for b in [b1, b2, b3]:
        b.pack(**options)

    g.mainloop()
    g.destroy()


def figure7():
    print 'Figure 17.5'

    g = Gui()
    options = dict(side=TOP, fill=X)
    b1 = g.bu(text='OK', command=g.quit, **options)
    b2 = g.bu(text='Cancel Command', **options)
    b3 = g.bu(text='Help', **options)

    g.mainloop()
    g.destroy()


def figure8():
    print 'Figure 17.6'

    g = Gui()
    options = dict(side=TOP, fill=X)

    # create the widgets
    g.fr()
    la = g.la(side=TOP, text='List of colors:')
    lb = g.lb(side=LEFT)
    sb = g.sb(side=RIGHT, fill=Y)
    g.endfr()

    bu = g.bu(side=BOTTOM, text='OK', command=g.quit)

    # fill the listbox with color names
    colors = []
    for line in open('/etc/X11/rgb.txt'):
        t = line.split('\t')
        name = t[-1].strip()
        colors.append(name)

    for color in colors:
        lb.insert(END, color)

    # tell the listbox and the scrollbar about each other
    lb.configure(yscrollcommand=sb.set)
    sb.configure(command=lb.yview)

    g.mainloop()
    g.destroy()


def figure9():
    print 'Figure 17.7 a'

    g = Gui()
    options = dict(side=LEFT)
    b1 = g.bu(text='OK', command=g.quit, **options)
    b2 = g.bu(text='Cancel', **options)
    b3 = g.bu(text='Help', **options)

    g.geometry('300x150')
    g.mainloop()


def figure10():
    print 'Figure 17.7 b'

    def pack(**options):
        for b in [b1, b2, b3]:
            b.pack(**options)

    pack(side=LEFT, fill=X, expand=1)

    g.mainloop()

def figure11():
    print 'Figure 17.7 c'

    options = dict(side=LEFT, fill=NONE, expand=0)
    b1.pack(**options)
    b2.pack(**options)

    # the override function is defined in Gui.py
    override(options, expand=1)
    b3.pack(**options)

    g.mainloop()

def figure12():
    print 'Figure 17.7 d'

    pack(**options)

    g.mainloop()

def figure13():
    print 'Figure 17.7 e'

    options = dict(side=LEFT, fill=BOTH, expand=1)
    pack(**options)

    g.mainloop()

def main():
    figure8()

main()
