"""This module is part of an exercise for
Think Python: an Introduction to Software Design

Copyright 2011 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import os
import sys
from subprocess import Popen

def spawn_popup(message, sender):
    """Launches a Popup in a subprocess."""
    cmd = ['python', 'Popup.py', message, sender]
    pid = Popen(cmd).pid
    return pid


def main(script):
    """Spawns three Popups."""

    # if you don't get this reference, see 
    # http://www.ibras.dk/montypython/episode03.htm

    for innuendo in ['Nudge, nudge', 'Snap, snap.', 'Grin, grin.']:
        print spawn_popup(innuendo, 'Norman')


if __name__ == '__main__':
    main(*sys.argv)

