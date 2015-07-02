"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""


def has_duplicates(t):
    """Checks whether any element appears more than once in a sequence.

    Simple version using a for loop.

    t: sequence
    """
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates2(t):
    """Checks whether any element appears more than once in a sequence.

    Faster version using a set.

    t: sequence
    """
    return len(set(t)) < len(t)


if __name__ == '__main__':
    t = [1, 2, 3]
    print has_duplicates(t)
    t.append(1)
    print has_duplicates(t)

    t = [1, 2, 3]
    print has_duplicates2(t)
    t.append(1)
    print has_duplicates2(t)

