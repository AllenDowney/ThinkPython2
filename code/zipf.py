"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import sys
import string

import matplotlib.pyplot as pyplot

from analyze_book import *


def rank_freq(hist):
    """Returns a list of tuples where each tuple is a rank
    and the number of times the item with that rank appeared.
    """
    # sort the list of frequencies in decreasing order
    freqs = hist.values()
    freqs.sort(reverse=True)

    # enumerate the ranks and frequencies 
    rf = [(r+1, f) for r, f in enumerate(freqs)]
    return rf


def print_ranks(hist):
    """Prints the rank vs. frequency data."""
    for r, f in rank_freq(hist):
        print r, f


def plot_ranks(hist, scale='log'):
    """Plots frequency vs. rank."""
    t = rank_freq(hist)
    rs, fs = zip(*t)

    pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('Zipf plot')
    pyplot.xlabel('rank')
    pyplot.ylabel('frequency')
    pyplot.plot(rs, fs, 'r-')
    pyplot.show()


def main(name, filename='emma.txt', flag='plot', *args):
    hist = process_file(filename, skip_header=True)

    # either print the results or plot them
    if flag == 'print':
        print_ranks(hist)
    elif flag == 'plot':
        plot_ranks(hist)
    else:
        print 'Usage: zipf.py filename [print|plot]'


if __name__ == '__main__':
    main(*sys.argv)
