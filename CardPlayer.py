#!/usr/bin/python

from Message import Message
from Neuron import Neuron
from Card import Card
from Deck import Deck


class CardSensor(Neuron):
    attrs = {"suit": "suits", "value": "values"}

    def __str__(self):
        return "{}, suit:\{{}\}, value:\{{}\}".format(Neuron.__str__(self), self.sensors["suit"], self.sensors["value"])

    def __init__(self, **kwds):
        self.sensors = dict.fromkeys(self.attrs.keys())
        for attr in self.attrs.keys():
            tgt = len(getattr(Card, self.attrs[attr])) - 1
            self.sensors[attr] = Message(tgt, tgt)
        Neuron.__init__(self, self.sensors.values())
        self.card = None

    def show(self, card):
        for attr in self.attrs.keys():
            self.sensors[attr].val = getattr(card, attr)


class CardPlayer(Neuron):

    def __init__(self, senses, picks):
        self.senses = senses
        self.picks = picks
        self.sensors = dict.fromkeys(self.senses)
        self.pickers = dict.fromkeys(self.picks)
        self.cards = {}
        self.picked = None

        for sense in self.sensors.keys():
            self.sensors[sense] = CardSensor()

        for pick in self.picks:
            self.pickers[pick] = Neuron(self.sensors.values())

        Neuron.__init__(self, self.pickers.values())

    def deal(self, card):
        if len(self.cards) >= len(self.senses):
            raise OverflowError("CardPlayer was dealt more cards than it can sense")
        idx = self.senses[len(self.cards)]
        self.cards[idx] = card
        self.sensors[idx].show(card)

    def train(self, amt):
        if self.picked is not None and self.pickers.keys().count(self.picked) > 0:
            self.pickers[self.picked].train(amt)

    def fire(self):
        self.val = float('inf')
        for pick in self.pickers:
            val = self.pickers[pick].fire()
            if val < self.val:
                self.val = val
                self.picked = pick
        return self.cards[self.picked]


def hand(p, d):
    c = dict.fromkeys(p.senses)
    p.cards = {}
    for sense in p.senses:
        c[sense] = d()
        p.deal(c[sense])
    v = p.fire()
    r = cmp(v, c["house"])
    p.train(r)
    print "> cards:{}, played:{}, result:{}".format(
        list(
            str("{}:{}".format(
                C[0],
                C[1]
            )) for C in c.items()
        ),
        v,
        {-1: "lost", 1: "won"}[r]
    )
    return {-1: "lost", 1: "won"}[r]


def game(p):
    d = Deck(shuffled=True)
    played = 0
    series = []
    while len(d) >= 3:
        series.append(hand(p, d))
        played +=1
    print ">> played {} hands, won {} times".format(played, series.count("won"))
    print ">> cards left in deck: [{}]".format(str(d))
    return series


if __name__ == "__main__":
    print "results: {}".format(game(CardPlayer(("left", "right", "house"), ("left", "right"))))
