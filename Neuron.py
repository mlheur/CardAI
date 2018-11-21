#!/usr/bin/python

from Synapse import Synapse
from Message import Message
import collections


class Neuron(Message):
    def __init__(self, inputs=None, bias=0, **kwds):
        self.synapses = set()
        self.bias = bias
        self.selected = None
        self.add(inputs)
        Message.__init__(self, **kwds)

    def fire(self):
        self.val = float('inf')
        for synapse in self.synapses:
            val = synapse.fire()
            if val < self.val:
                self.val = val
                self.selected = synapse
        return Message.bias(self.val, self.bias)

    def train(self, amt):
        if isinstance(amt, bool) and amt is False:
            amt = -1
        if not isinstance(amt, int):
            return
        self.bias += amt
        if self.selected is not None:
            self.selected.train(amt)

    def add(self, inputs):
        if isinstance(inputs, collections.Iterable):
            for inp in inputs:
                self.add(inp)
        elif isinstance(inputs, Message):
            self.synapses.add(Synapse(inputs))
        elif isinstance(inputs, Synapse):
            self.synapses.add(inputs)
        else:
            raise TypeError("cannot add type {} as a neural input".format(type(inputs)))
