"""This module contains code from
Think Python: an Introduction to Software Design
Allen B. Downey

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

This program requires Gui.py, which is part of
Swampy; you can download it from thinkpython.com/swampy.

"""

from Tkinter import NW
import Gui
import PokerHand
import ImageTk


class Table(Gui.Gui):
    """A Table displays a green canvas and a control area."""

    def __init__(self):
        Gui.Gui.__init__(self)
        self.cardset = None            # the images used to display cards
        self.views = {}                # map from Hands to HandViews
        self.setup()

    def setup(self):
        self.ca_width = 100
        self.ca_height = 100
        
        # left frame
        self.row()
        self.canvas = self.ca(width=self.ca_width, height=self.ca_height,
                              bg='dark green', transforms=[])

        # right frame
        self.col([1,1,1])
        self.bu('Quit', command=self.quit)
        self.bu('Deal', command=self.deal_hand)
        self.bu('Print', command=self.canvas.dump)

    def set_cardset(self, cardset, numhands=6, numcards=9):
        """associate a cardset with this table, which has the
        effect of changing the size of the canvas and setting
        up the coordinate Transform"""
        self.cardset = cardset
        width = self.cardset.width
        height = self.cardset.height
        self.canvas.add_transform(TableTransform(width, height))
        self.canvas.configure(width=width*numcards, height=height*numhands)

    def deal_hand(self, numcards=7):
        """Deal one hand and create a HandView."""

        # shuffle the deck
        deck = PokerHand.Deck()
        deck.shuffle()

        # deal the cards 
        hand = PokerHand.PokerHand()
        deck.move_cards(hand, numcards)

        # display the Hand
        view = HandView(hand, self)
        view.draw(0, 0)
        self.views[hand] = view

    def clear(self):
        """delete the graphical representation of the HandViews,
        then delete the HandViews"""
        for view in self.views.values():
            view.delete()
        self.views = {}


class TableTransform(Gui.Transform):
    """transform coordinates so that the x-axis is in units of card widths
    and the y-axis is in units of card heights.  The origin is in the
    upper left corner, and the y-axis points down."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def trans(self, p):
        x = p[0] * self.width
        y = p[1] * self.height
        return [x, y]


class Cardset(dict):
    """A cardset is a dictionary that maps a tuple (suit,rank) onto
    an Image that depicts the card.  In addition, the dictionary
    contains a key 'back' that maps to an Image that depicts the
    back of the card."""

    def __init__(self, dir=None, ext='gif'):
        """create a cardset, reading cards from the given directory"""
        dict.__init__(self)
        if dir:
            self.read_cards(dir, ext)

    def read_cards(self, dir, ext='gif'):
        suits = 'cdhs'
        for rank in range(1,14):
            for suit in range(4):
                filename = '%s/%.2d%s.%s' % (dir, rank, suits[suit], ext)
                image = ImageTk.PhotoImage(file=filename)
                self[suit,rank] = image

        filename = '%s/back01.gif' % (dir)
        try:
            image = ImageTk.PhotoImage(file=filename)
            self['back'] = image
        except:
            pass

        # cardset keeps track of the width and height of the cards
        self.width = image.width()
        self.height = image.height()

    def lookup(self, card):
        """lookup the given card and return the Image that depicts it"""
        return self[card.suit, card.rank]

class HandView:
    """A HandView object represents a Hand being displayed on a Table"""
    
    def __init__(self, hand, table):
        self.hand = hand
        self.table = table

    def draw(self, x=0, y=0):
        """draw the hand at the given location on the table.
        the Tk tag for this item is a string based on the object id"""

        self.tag = 'HandView%d' % id(self)
        cardset = self.table.cardset
        width = cardset.width
        height = cardset.height
        for card in self.hand.cards:
            self.draw_card(card, x, y)
            x += 1

        # display the hand's label next to the hand
        self.table.canvas.text([x, y], self.hand.label,
                               fill='white', anchor=NW, tag=self.tag)

    def draw_card(self, card, x, y):
        """draw a single card at the given position"""
        image = self.table.cardset.lookup(card)
        self.table.canvas.image([x, y], image, anchor=NW, tag=self.tag)

    def move(self, dx=0, dy=0):
        """move the entire handset right by dx and down by dy"""
        self.table.move_item(self.tag, dx, dy)

    def delete(self):
        """remove the graphical representation of this HandView"""
        self.table.canvas.delete(self.tag)

    
def main(name, cardstyle='tuxedo', *args):
    table = Table()
    cardset = Cardset('cardsets/cardset-' + cardstyle)
    table.set_cardset(cardset)    
    table.mainloop()
    
if __name__ == '__main__':
    import sys
    main(*sys.argv)
