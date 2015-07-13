"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import sys

import matplotlib.pyplot as plt

from analyze_book1 import process_file


def rank_freq(hist):
    """Returns a list of (rank, freq) tuples.

    hist: map from word to frequency

    returns: list of (rank, freq) tuples
    """
    # sort the list of frequencies in decreasing order
    freqs = list(hist.values())
    freqs.sort(reverse=True)

    # enumerate the ranks and frequencies 
    rf = [(r+1, f) for r, f in enumerate(freqs)]
    return rf


def print_ranks(hist):
    """Prints the rank vs. frequency data.

    hist: map from word to frequency
    """
    for r, f in rank_freq(hist):
        print(r, f)


def plot_ranks(hist, scale='log'):
    """Plots frequency vs. rank.

    hist: map from word to frequency
    scale: string 'linear' or 'log'
    """
    t = rank_freq(hist)
    rs, fs = zip(*t)

    plt.clf()
    plt.xscale(scale)
    plt.yscale(scale)
    plt.title('Zipf plot')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    plt.plot(rs, fs, 'r-', linewidth=3)
    plt.show()


def main(script, filename='emma.txt', flag='plot'):
    hist = process_file(filename, skip_header=True)

    # either print the results or plot them
    if flag == 'print':
        print_ranks(hist)
    elif flag == 'plot':
        plot_ranks(hist)
    else:
        print('Usage: zipf.py filename [print|plot]')


if __name__ == '__main__':
    main(*sys.argv)
