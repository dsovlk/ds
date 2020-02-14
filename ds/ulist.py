#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (C) 2020 dvolkov

from node import Node


class UnorderedList:
    """
    Implements Unordered Lists
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        """
        Add node to the list
        """
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp

    def remove(self):
        """
        Return head node and Remove it from the list
        """
        if self.size() > 0:
            temp = self.head
            self.head = self.head.get_next()
            return temp
        else:
            return None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()

        return count


ul = UnorderedList()
ul.add('A')
ul.add('B')
ul.add('C')
print ul.size()
ul.remove()
print ul.size()
ul.remove()
print ul.size()
ul.remove()
print ul.size()
ul.remove()
print ul.size()
