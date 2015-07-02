"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

    http://www.cartalk.com/content/puzzler/transcripts/200813
"""

def str_fill(i, len):
    """return the integer (i) written as a string with at least
    (len) digits"""
    return str(i).zfill(len)


def are_reversed(i, j):
    """ return True if the integers i and j, written as strings,
    are the reverse of each other"""
    return str_fill(i,2) == str_fill(j,2)[::-1]


def num_instances(diff, flag=False):
    """returns the number of times the mother and daughter have
    pallindromic ages in their lives, given the difference in age.
    If flag==True, prints the details."""
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
            count = count + 1
            if flag:
                print daughter, mother
        if mother > 120:
            break
        daughter = daughter + 1
    return count
    

def check_diffs():
    """enumerate the possible differences in age between mother
    and daughter, and for each difference, count the number of times
    over their lives they will have ages that are the reverse of
    each other."""
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print diff, n
        diff = diff + 1

print 'diff  #instances'
check_diffs()

print
print 'daughter  mother'
num_instances(18, True)
