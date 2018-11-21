#!/usr/bin/python
################################################################################

from Card import Card
import random

class Deck:

    def __init__(self, shuffled=False, empty=False):
        self.cards = list()
        if not empty:
            self.build()
        if shuffled:
            self.shuffle()

    def __str__(self):
        return ",".join(str(card) for card in self.cards)

    def __call__(self, amt=1):
        if amt == 1:
            return self.cards.pop()
        result = list()
        while amt > 1:
            amt -= 1
            result.insert(self.cards.pop())
        return result

    def __len__(self):
        return len(self.cards)

    def build(self):
        self.cards = list()
        for s in Card.suits:
            for v in Card.values: self.cards.append(Card(s, v))

    def shuffle(self): random.shuffle(self.cards)

