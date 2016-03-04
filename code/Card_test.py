"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import unittest
from Card import Card, Deck


class Test(unittest.TestCase):

    def testDeckRemove(self):
        deck = Deck()
        card23 = Card(2, 3)
        deck.remove_card(card23)


if __name__ == "__main__":
    unittest.main()
