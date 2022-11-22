import unittest

from src.example_package_reyniel26.example import add_one


class TestIncrement(unittest.TestCase):

    def test_add_to_2(self):
        self.assertEqual(add_one(2), 3, "Should be 3")

    def test_add_to_20(self):
        self.assertEqual(add_one(20), 21, "Should be 21")