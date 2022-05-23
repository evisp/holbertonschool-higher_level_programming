#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_list_ints(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([1, 2, 1]), 2)
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-1, -1, -1]), -1)

    def test_list_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)
        self.assertEqual(max_integer([-1.1, 0, 1]), 1)
        self.assertEqual(max_integer([-1, -7.2, 3]), 3)

    def test_string(self):
        self.assertEqual(max_integer("Jack Sparrow"), 'w')
        self.assertEqual(max_integer(["Jack", "Sparrow"]),"Sparrow")
        self.assertEqual(max_integer(""), None)

