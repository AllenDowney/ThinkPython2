"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import random


def sort_by_length(words):
    """Sort a list of words in reverse order by length.

    This is the version in the book; it is stable in the sense that
    words with the same length appear in the same order

    words: list of strings

    Returns: list of strings
    """
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res


def sort_by_length_random(words):
    """Sort a list of words in reverse order by length.

    This is the solution to the exercise.  It is unstable in the
    sense that if two words have the same length, their order in
    the output list is random.

    It works by extending the list of tuples with a column of
    random numbers; when there is a tie in the first column,
    the random column determines the output order.

    words: list of strings

    Returns: list of strings
    """
    t = []
    for word in words:
        t.append((len(word), random.random(), word))

    t.sort(reverse=True)

    res = []
    for length, _, word in t:
        res.append(word)
    return res


if __name__ == '__main__':
    words = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

    t = sort_by_length_random(words)
    for x in t:
        print(x)
