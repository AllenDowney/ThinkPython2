"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import shelve
import sys

from anagram_sets import *


def store_anagrams(filename, ad):
    """Stores the anagrams in ad in a shelf.

    filename: string file name of shelf
    ad: dictionary that maps strings to list of anagrams
    """
    shelf = shelve.open(filename, 'c')

    for word, word_list in ad.iteritems():
        shelf[word] =  word_list

    shelf.close()


def read_anagrams(filename, word):
    """Looks up a word in a shelf and returns a list of its anagrams.

    filename: string file name of shelf
    word: word to look up
    """
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []


def main(name, command='store'):
    if command == 'store':
        ad = all_anagrams('words.txt')
        store_anagrams('anagrams.db', ad)
    else:
        print read_anagrams('anagrams.db', command)



if __name__ == '__main__':
    main(*sys.argv)
    
