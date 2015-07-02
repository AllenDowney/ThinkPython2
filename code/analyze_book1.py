"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import random
import string

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        process_line(line, hist)

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_line(line, hist):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: histogram (map from word to frequency)
    """
    # TODO: rewrite using Counter

    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    strippables = string.punctuation + string.whitespace

    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(strippables)
        word = word.lower()

        # update the histogram
        hist[word] = hist.get(word, 0) + 1


def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    # TODO: reimplement using Counter
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    # TODO: rewrite using Counter
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq)

    return random.choice(t)


def main():
    hist = process_file('emma.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    words = process_file('words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()


