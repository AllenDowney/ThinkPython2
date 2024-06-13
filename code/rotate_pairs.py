"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from rotate import rotate_word


def make_word_list():
    """Read the words in words.txt and return a list
    that contains the words."""
    with open('words.txt') as fin:
        word_list = []
        for line in fin:
            word = line.strip().lower()
            word_list.append(word)
            
    return word_list


def rotate_pairs(word_list):
    """Return list of all rotate pairs found in word_list.
    word_list: list of words
    """
    rotate_pairs = {}

    for word in word_list:
        first_letter = word[0]
        if first_letter.isupper():
            ref_letter = ord('A')
        elif first_letter.islower():
            ref_letter = ord('a')
            
        # Create a rotated word which always starts with "A" or "a"
        # and use it as a key to store the word in the rotate_pairs dict.
        rotated_word = rotate_word(word, ref_letter - ord(first_letter))
        rotate_pairs.setdefault(rotated_word, []).append(word)
        
    # Rotate pairs are contained in the lists that have more than one word.
    rotate_pairs = [item for item in rotate_pairs.values() if len(item) > 1]
    return rotate_pairs


if __name__ == '__main__':
    word_list = make_word_list()
    all_rotate_pairs = rotate_pairs(word_list)
