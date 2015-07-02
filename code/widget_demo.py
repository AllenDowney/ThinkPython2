"""Solution to an exercise from
Think Python: An Introduction to Software Design

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

This program requires Gui.py, which is part of
Swampy; you can download it from thinkpython.com/swampy.

This program demonstrates how to use the Gui module
to create and operate on Tkinter widgets.

The documentation for the widgets is at
http://www.pythonware.com/library/tkinter/introduction/
"""

from swampy.Gui import *

# create the Gui: the debug flag makes the frames visible
g = Gui(debug=False)

# the topmost structure is a row of widgets
g.row()

# FRAME 1

# the first frame is a column of widgets
g.col()

# la is for label
la1 = g.la(text='This is a label.')

# en is for entry
en = g.en()
en.insert(END, 'This is an entry widget.')

la2 = g.la(text='')

def press_me():
    """this callback gets invoked when the user presses the button"""
    text = en.get()
    la2.configure(text=text)

# bu is for button
bu = g.bu(text='Press me', command=press_me)

# end of the first frame
g.endcol()


# FRAME 2

g.col()

# ca is for canvas
ca = g.ca(width=200, height=200)

item1 = ca.circle([0, 0], 70, 'red')
item2 = ca.rectangle([[0, 0], [60, 60]], 'blue')
item3 = ca.text([0, 0], 'This is a canvas.', 'white')

# mb is for menubutton
mb = g.mb(text='Choose a color')

def set_color(color):
    ca.itemconfig(item2, fill=color)

# mi is for menuitem
for color in ['red', 'green', 'blue']:

    # Callable is an object that can be used like a function
    g.mi(mb, color, command=Callable(set_color, color))
    
g.endcol()


# FRAME 3

g.col()

def get_selection():
    t = lb.curselection()
    try:
        index = int(t[0])
        color = lb.get(index)
        return color
    except:
        return None

def print_selection(event):
    print get_selection()

def apply_color():
    color = get_selection()
    if color:
        ca.itemconfig(item1, fill=color)

la = g.la(text='List of colors:')

g.row()
# lb is for listbox
lb = g.lb()
lb.bind('<ButtonRelease-1>', print_selection)

# sb is for scrollbar
sb = g.sb()
g.endrow()


bu = g.bu(text='Apply color', command=apply_color)
g.endcol()

# fill the listbox with color names
fp = open('/etc/X11/rgb.txt')
fp.readline()

for line in fp:
    t = line.split('\t')
    name = t[2].strip()
    lb.insert(END, name)

# tell the listbox and the scrollbar about each other
lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)


# FRAME 4

g.col()

# te is for text entry
te = g.te(height=5, width=40)
te.insert(END, "This is a Text widget.\n")
te.insert(END, "It's like a little text editor.\n")
te.insert(END, "It has more than one line, unlike an Entry widget.\n")

# st is for scrollable text
st = g.st()
st.text.configure(height=5, width=40)

st.text.insert(END, "This is a Scrollable Text widget.\n")
st.text.insert(END, "It is defined in Gui.py\n")

for i in range(100):
    st.text.insert(END, "All work and no play.\n")

g.endcol()


# FRAME 5

# gr is for grid: start a grid with three columns
# the rweights control how extra space is divided among the rows
g.gr(3, rweights=[1,1,1])

for i in range(1, 10):
    g.bu(text=str(i))

g.endgr()


# FRAME 6

g.col()

def print_var(obj):
    print obj.var.get()

g.la(text='Font:')
fontsize = IntVar()

# rb is for radiobutton
for size in [10, 12, 14, 16, 18]:
    rb = g.rb(text=str(size), variable=fontsize, value=size)
    rb.configure(command=Callable(print_var, rb))

# cb is for checkbutton
b1 = g.cb(text='Bold')
b1.configure(command=Callable(print_var, b1))

b2 = g.cb(text='Italic')
b2.configure(command=Callable(print_var, b2))

g.endcol()

g.mainloop()
