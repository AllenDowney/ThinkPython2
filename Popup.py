"""This module is part of an exercise for
Think Python: an Introduction to Software Design

Copyright 2011 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import sys

from swampy.Gui import Gui

class Popup(Gui):
    """Creates a top-level window with a message."""

    def __init__(self, message, sender):
        Gui.__init__(self)
        self.title('Popup')
        self.la(text='From: %s' % sender)
        self.la(text=message)
        self.bu(text='Close', command=self.destroy)
        self.mainloop()


def main(script, message='default message', sender='unknown', *args):
    Popup(message, sender)


if __name__ == '__main__':
    main(*sys.argv)
