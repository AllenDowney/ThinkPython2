"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def first(word):
    """Returns the first character of a string."""
    return word[0]


def last(word):
    """Returns the last of a string."""
    return word[-1]


def middle(word):
    """Returns all but the first and last characters of a string."""
    return word[1:-1]


def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True #this returns true if the length of the word is 0 or 1 because words might be odd or even-numbered. 
    #An even-numbered word, after line 37 will have a length of 0. An odd-numbered word will have a length of 1 at the final call of line 37.
    if first(word) != last(word):
        return False #if this condition is met, line 37 will not be run, and the function will terminate.
    return is_palindrome(middle(word))


print(is_palindrome('allen'))
print(is_palindrome('bob'))
print(is_palindrome('otto'))
print(is_palindrome('redivider'))

