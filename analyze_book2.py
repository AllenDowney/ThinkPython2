"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import string
import random

from analyze_book import *


def subtract(d1, d2):
    """Returns a set of all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    return set(d1) - set(d2)


if __name__ == '__main__':
    hist = process_file('emma.txt', skip_header=True)
    print 'Total number of words:', total_words(hist)
    print 'Number of different words:', different_words(hist)

    t = most_common(hist)
    print 'The most common words are:'
    for freq, word in t[0:20]:
        print word, '\t', freq

    words = process_file('words.txt', skip_header=False)

    diff = subtract(hist, words)
    print "The words in the book that aren't in the word list are:"
    for word in diff:
        print word,

    print "\n\nHere are some random words from the book"
    for i in range(100):
        print random_word(hist),

