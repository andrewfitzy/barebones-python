# Standard Library
import unittest

# From apps
from math_operations import add_numbers


class MyTestCase(unittest.TestCase):
    def test_add_numbers(self):
        param_1 = 1
        param_2 = 2

        result = add_numbers(param_1, param_2)

        assert result == 3, "The result should be 3 when adding 1 and 2"
