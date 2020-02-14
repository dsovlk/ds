#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (C) 2020 dvolkov


class Node:
    """
    Node  is a helper class for Unordered/Ordered Lists
    """

    def __init__(self, data=None):
        self.data = data
        self.next_node = None

    def set_data(self, data):
        self.data = data

    def get_data (self):
        return self.data

    def set_next(self, next_node):
        self.next_node = next_node

    def get_next(self):
        return self.next_node
