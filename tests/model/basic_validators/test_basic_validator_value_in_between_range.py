import unittest
from app.validator.basic_validator import value_in_between_range
from typing import Final

MIN_VALUE: Final[int] = 0
MAX_VALUE: Final[int] = 10


class BasicValidatorHasValueBetween(unittest.TestCase):
    def test_when_value_is_in_range(self):
        value = 9
        self.assertTrue(value_in_between_range(MIN_VALUE, MAX_VALUE, value))

    def test_when_value_is_not_in_range(self):
        value = 10
        self.assertFalse(value_in_between_range(MIN_VALUE, MAX_VALUE, value))

    def test_when_min_is_greater_than_max(self):
        min_value = 100
        value = 5
        self.assertRaises(ValueError, lambda: value_in_between_range(min_value, MAX_VALUE, value))
