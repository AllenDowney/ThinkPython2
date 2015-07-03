"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def has_palindrome(i, start, length):
    """Checks if the string representation of i has a palindrome.

    i: integer
    start: where in the string to start
    length: length of the palindrome to check for
    """
    s = str(i)[start:start+length]
    return s[::-1] == s

    
def check(i):
    """Checks if the integer (i) has the desired properties.

    i: int
    """
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))


def check_all():
    """Enumerate the six-digit numbers and print any winners.
    """
    i = 100000
    while i <= 999996:
        if check(i):
            print(i)
        i = i + 1


print('The following are the possible odometer readings:')
check_all()
print()


