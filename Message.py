#!/usr/bin/python

def mixmax(n, top, bot):
    assert top - bot, "mixmax only works on a range"
    return float(n - bot) / (top - bot)


class Message:

    @staticmethod
    def bias(val, bias):
        return float(val) / (2 ** bias)

    def __init__(self, tgt=0, top=1, bot=0, val=float('inf')):
        self.tgt = tgt
        self.top = top
        self.bot = bot
        self.val = val

    def __str__(self):
        return "message:\{tgt:{},top:{},bot:{},val:{}\}".format(self.tgt, self.top, self.bot, self.val)

    def fire(self):
        return abs(mixmax(1+self.val, 1+self.top, self.bot) - mixmax(self.tgt, self.top, self.bot))

    def train(self, amt):
        pass
