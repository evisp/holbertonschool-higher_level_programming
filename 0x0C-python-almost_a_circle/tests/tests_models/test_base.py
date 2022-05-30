#!/usr/bin/python3
""" test base script """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ class to test , Base """

    def setUp(self):
        """ This is called immediately before calling the test method """
        Base._Base__nb_objects = 0

    def test_zero(self):
        """ test"""
        base = Base(0)
        self.assertEqual(base.id, 0)

    def test_integer(self):
        """ test"""
        base = Base(18)
        self.assertEqual(base.id, 18)

    def test_negative(self):
        """ test """
        base = Base(-8)
        self.assertEqual(base.id, -8)

    def test_string(self):
        """ test """
        base = Base("string")
        self.assertEqual(base.id, "string")


    def test_none(self):
        """ test """
        base = Base(None)
        self.assertEqual(base.id, 1)

    def test_dictionary(self):
        """ test """
        base = Base({"hello": "World"})
        self.assertEqual(base.id, {"hello": "World"})

    def test_float(self):
        """ test """
        base = Base(5.3)
        self.assertEqual(base.id, 5.3)

    def test_list(self):
        """ test """
        base = Base([1, 2, 3])
        self.assertEqual(base.id, [1, 2, 3])

    def test_test(self):
        """ test """
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
