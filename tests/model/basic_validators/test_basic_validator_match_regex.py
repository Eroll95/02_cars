import unittest
from app.validator.validator import matches_regex


class BasicValidatorMatchRegex(unittest.TestCase):
    def test_regex_correct_value(self):
        capital_regex = r'^[A-Z]+$'
        correct_value = 'AUDI'
        self.assertTrue(matches_regex(capital_regex, correct_value))

    def test_regex_incorrect_values(self):
        capital_regex = r'^[A-Z]+$'
        self.assertFalse(matches_regex(capital_regex, ''))
        self.assertFalse(matches_regex(capital_regex, 'audi'))
        self.assertFalse(matches_regex(capital_regex, 'AUDI3'))
        self.assertFalse(matches_regex(capital_regex, 'AUD-I'))
        self.assertFalse(matches_regex(capital_regex, 'ALFA ROMEO'))
