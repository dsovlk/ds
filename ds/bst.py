#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (C) 2020 dvolkov


from bnode import BNode


class BinarySearchTree:
    """
    Implements binary search tree. Current supports only numbers
    """

    def __init__ (self):
        self.root = None

    def insert(self, data):
        """
        Add new data into existing tree
        :param data: value to keep
        :return:
        """
        curr_node = BNode(data)

        if self.root is None:  # Empty tree
            self.root = curr_node

        else:
            self._insert(self.root, curr_node)

    def _insert(self, root_node, curr_node):
        """
        Helper method - implements new node insert
        :param root_node: current pos
        :param curr_node:
        :return:
        """
        if root_node is None:
            root_node = curr_node
        else:
            if curr_node.get_data() < root_node.get_data():
                if root_node.left is None:
                    root_node.left = curr_node
                else:
                    self._insert(root_node.left, curr_node)

            elif curr_node.get_data() > root_node.get_data():
                if root_node.right is None:
                    root_node.right = curr_node
                else:
                    self._insert(root_node.right, curr_node)

            else:
                print ('Data already exists in the tree')
        return

    def printInOrder(self):

        if self.root:
            self._printInOrder(self.root)

    def _printInOrder(self, node):

        if node:
            self._printInOrder(node.left)
            print(str(node.get_data()))
            self._printInOrder(node.right)

    def contains(self, data):
        """
        Verify is data in the tree
        :param data:
        :return: True if data in the tree otherwise False
        """

        if self.root:
            return self._contains(self.root, data)
        else:
            return False

    def _contains(self, root, data):

        if root:
            if root.get_data() == data:
                return True
            elif data > self.root.get_data():
                return self._contains(root.right, data)
            else:
                return self._contains(root.left, data)
        else:
            return False


bst = BinarySearchTree()
bst.insert(3)
bst.insert(5)
bst.insert(2)
bst.insert(6)

bst.printInOrder()

print bst.contains(10)
print bst.contains(2)
