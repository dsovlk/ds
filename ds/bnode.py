#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (C) 2020 dvolkov


class BNode:
    """
    Node  is a helper class for Binary Search Tree
    """

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
