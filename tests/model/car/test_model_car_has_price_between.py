import unittest
from decimal import Decimal
from tests.data import CAR_1


class CarModelHasPriceBetween(unittest.TestCase):
    def test_when_price_is_in_range(self):
        min_price = Decimal('50')
        max_price = Decimal('150')
        self.assertTrue(CAR_1.has_price_between(min_price, max_price))

    def test_when_price_is_not_in_range(self):
        min_price = Decimal('150')
        max_price = Decimal('250')
        self.assertFalse(CAR_1.has_price_between(min_price, max_price))
