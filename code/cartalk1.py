"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.
    
    word: string

    returns: bool
    """
    word_len = len(word)
    if word_len < 6:
        return False
    for i in range(word_len - 6):
        if word[i] == word[i+1]:
            if word[i+2] == word[i+3] and word[i+4] == word[i+5]:
                return True
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')


