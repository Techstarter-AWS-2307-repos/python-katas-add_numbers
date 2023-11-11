import unittest
import os
from add_numbers import add_two_numbers


class TestAddTwoNumbers(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(
            os.path.isfile("add_numbers.py"), "add_numbers.py does not exist"
        )

    def test_addition(self):
        self.assertEqual(add_two_numbers(1, 2), 3)
        self.assertEqual(add_two_numbers(-1, 1), 0)
        self.assertEqual(add_two_numbers(0, 0), 0)
