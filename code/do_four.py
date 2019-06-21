"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def do_twice(func, arg):
    """Runs a function twice.

    func: function object
    arg: argument passed to the function
    """
    func(arg)
    func(arg)


def print_twice(arg):
    """Prints the argument twice.

    arg: anything printable
    """
    print(arg)
    print(arg)


def do_four(func, arg):
    """Runs a function four times.

    func: function object
    arg: argument passed to the function
    """
    do_twice(func, arg)
    do_twice(func, arg)


do_twice(print, 'spam')
print('')

do_four(print, 'spam')
