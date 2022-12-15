import unittest
from tests.data import BASIC_INFO_1, WHEEL_INFO_1
from app.validator.validator import ValidateWheelData, ValidateBasicData
from decimal import Decimal


class MyTestCase(unittest.TestCase):

    def test_object_has_correct_wheel_type(self):
        self.assertTrue(ValidateWheelData.validate_wheel(WHEEL_INFO_1))

    def test_object_has_correct_name(self):
        self.assertTrue(ValidateBasicData.validate_name(BASIC_INFO_1))

    def test_object_has_correct_price(self):
        self.assertTrue(ValidateBasicData.validate_price(BASIC_INFO_1))

    def test_object_has_correct_price_instance(self):
        self.assertIsInstance(BASIC_INFO_1.data['price'], int)

