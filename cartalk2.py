"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

    http://www.cartalk.com/content/puzzler/transcripts/200803
"""

def has_palindrome(i, start, len):
    """return True if the integer i, when written as a string,
    contains a palindrome with length (len), starting at index (start).
    """
    s = str(i)[start:start+len]
    return s[::-1] == s
    
def check(i):
    """check whether the integer (i) has the properties described
    in the puzzler
    """
    return (has_palindrome(i, 2, 4)   and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))

def check_all():
    """enumerate the six-digit numbers and print any that satisfy the
    requirements of the puzzler"""

    i = 100000
    while i <= 999999:
        if check(i):
            print i
        i = i + 1

print 'The following are the possible odometer readings:'
check_all()
print


