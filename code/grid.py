"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""





"""Create variables for the addition and subtraction operators 
and print them in the order and number of times in which they appear on a line."""

def operators():
    add = "+ "
    sub = "- " * 4
    
    print(add,sub,add,sub,add)


"""Create a function that prints the straight beams and adds the appropriate amount of space between them"""

def straight_beams():
    print("|" + " " * 11 + "|" + " " * 11 + "|")

"""Create a function that would repeat the straight_beams function 4 times when passed as an argument"""

def do_four_times(func):
    func()
    func()
    func()
    func()

"""The final function that arranges the previous functions in the order that creates the grid"""

def grid_maker():
    operators()
    do_four_times(straight_beams)
    operators()
    do_four_times(straight_beams)
    operators()


grid_maker()