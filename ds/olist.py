#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (C) 2020 dvolkov


from node import Node


class OrderedList:
    """
    Implements Ordered Lists (currently support numbers only)
    head -> 17 -> 20 -> 25
    """

    def __init__(self):
        self.head = None

    def add(self, item):
        current = self.head
        previous = None
        found = False

        while current is not None and not found:
            if item > current.get_data():
                previous = current
                current = current.get_next()
            else:
                found = True

        temp = Node(item)
        if previous is not None:
            temp.set_next(current)
            previous.set_next(temp)
        else:                 # Empty list or element have to be added to the start
            if found:   # First element
                temp.set_next(current)
            self.head = temp

    def get(self):
        items = []
        current = self.head
        while current is not None:
            items.append(current.get_data())
            current = current.get_next()
        return items

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

o = OrderedList()

o.add(20)
print o.get()

o.add(50)
print o.get()

o.add(40)
print o.get()

o.add(30)
print o.get()

o.add(10)
print o.get()

o.add(11)
print o.get()

o.add(60)
print o.get()

