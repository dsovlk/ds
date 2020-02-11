#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (C) 2020 dvolkov


class Queue:
    """
    Fist In Fist Out Data Structure
    """

    def __init__(self):
        self.items = []

    def enqueue (self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop() if not self.isEmpty() else None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if len(self.items) > 0:
            return False
        else:
            return True
