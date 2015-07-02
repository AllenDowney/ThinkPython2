"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(arg):
    print arg
    print arg

do_twice(print_twice, 'spam')
print ''

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_four(print_twice, 'spam')
print ''
