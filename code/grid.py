"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

# here is a mostly-straightforward solution to the
# two-by-two version of the grid.

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print '+ - - - -',

def print_post():
    print '|        ',

def print_beams():
    do_twice(print_beam)
    print '+'

def print_posts():
    do_twice(print_post)
    print '|'

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()
    

# here is a less-straightforward solution to the
# four-by-four grid

def one_four_one(f, g, h):
    f()
    do_four(g)
    h()

def print_plus():
    print '+',

def print_dash():
    print '-',

def print_bar():
    print '|',

def print_space():
    print ' ',

def print_end():
    print

def nothing():
    "do nothing"

def print1beam():
    one_four_one(nothing, print_dash, print_plus)

def print1post():
    one_four_one(nothing, print_space, print_bar)

def print4beams():
    one_four_one(print_plus, print1beam, print_end)

def print4posts():
    one_four_one(print_bar, print1post, print_end)

def print_row():
    one_four_one(nothing, print4posts, print4beams)

def print_grid():
    one_four_one(print4beams, print_row, nothing)

print_grid()

comment = """
After writing a draft of the 4x4 grid, I noticed that many of the
functions had the same structure: they would do something, do
something else four times, and then do something else once.

So I wrote one_four_one, which takes three functions as arguments; it
calls the first one once, then uses do_four to call the second one
four times, then calls the third.

Then I rewrote print1beam, print1post, print4beams, print4posts,
print_row and print_grid using one_four_one.

Programming is an exploratory process.  Writing a draft of a program
often gives you insight into the problem, which might lead you to
rewrite the code to reflect the structure of the solution.

--- Allen
"""

print comment
