#!/usr/bin/python

from Message import Message


class Synapse:

    def __init__(self, msg, bias=0):
        assert isinstance(msg, Message), "synapse must take a Message class"
        self.msg = msg
        self.bias = bias

    def __str__(self):
        return "msg:{}, bias:{}".format(self.msg, self.bias)

    def fire(self):
        return Message.bias(self.msg.fire(), self.bias)

    def train(self, amt):
        self.msg.train(amt)
