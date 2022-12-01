import unittest
from tests.data import CAR_1


class CarModelHasPowerBetween(unittest.TestCase):
    def test_when_power_is_in_range(self):
        min_power = 50
        max_power = 300
        self.assertTrue(CAR_1.engine.has_power_between(min_power, max_power))

    def test_when_power_is_not_in_range(self):
        min_power = 301
        max_power = 1000
        self.assertFalse(CAR_1.engine.has_power_between(min_power, max_power))
