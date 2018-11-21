#!/usr/bin/python


class Card:
    suits = ("C", "D", "H", "S")
    values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K")

    def __init__(self, suit, value):
        self.suit = Card.suits.index(suit)
        self.value = Card.values.index(value)
        
    def __str__(self): return Card.values[self.value] + Card.suits[self.suit]
    
    def __cmp__(self, subject):
        ret = cmp(self.value, subject.value)
        if ret == 0:
            ret = cmp(self.suit, subject.suit)
        return ret
