#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (C) 2020 dvolkov

import unittest
from ds import Stack


class StackTest(unittest.TestCase):

    def setUp(self):
        self.s = Stack()

    def tearDown(self):
        while not self.s.isEmpty():
            self.s.pop()

    def test_push(self):
        value = 'A'
        self.s.push(value)
        self.assertEqual(1, self.s.size())
        print self.s.get()
        x = self.s.pop()
        print self.s.get()
        self.assertEqual(value, x)
        self.assertEqual(0, self.s.size())

    def test_peek(self):
        self.s.push('A')
        self.s.push('B')
        x = self.s.peek()
        self.assertEqual('B', x)
        self.assertEqual(2, self.s.size())

    def test_empty(self):
            self.assertEqual(self.s.peek(), None)


if __name__ == '__main__':
    unittest.main()

