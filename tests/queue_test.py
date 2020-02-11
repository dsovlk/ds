#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (C) 2020 dvolkov

import unittest
from ds import Queue


class QueueTest(unittest.TestCase):

    def setUp(self):
        self.q = Queue()

    def tearDown(self):
        while not self.q.isEmpty():
            self.q.dequeue()

    def test_enqueue(self):
        value = 'A'
        self.q.enqueue(value)
        self.assertEqual(1, self.q.size())


if __name__ == '__main__':
    unittest.main()

