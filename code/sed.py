"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import sys


def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.

    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    try:
        fin = open(source, 'r')
        fout = open(dest, 'w')

        for line in fin:
            line = line.replace(pattern, replace)
            fout.write(line)

        fin.close()
        fout.close()
    except:
        print 'Something went wrong.'


def main(name):
    pattern = 'pattern'
    replace = 'replacendum'
    source = name
    dest = name + '.replaced'
    sed(pattern, replace, source, dest)


if __name__ == '__main__':
    main(*sys.argv)
