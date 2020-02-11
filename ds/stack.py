#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (C) 2020 dvolkov


class Stack:
    """
    Stack Data Structure. Last In First Out (LIFO)
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def get(self):
        return self.items

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if len(self.items) > 0:
            return False
        else:
            return True

