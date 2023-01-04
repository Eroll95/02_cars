import pytest
import unittest
from tests.data.validator_obj_data import BASIC_INFO_1, BASIC_INFO_2, BASIC_INFO_3, BASIC_INFO_4
from app.validator.validator import ValidateBasicData


class ValidatorValidateBasicData(unittest.TestCase):

    # TESTS Name

    def test_object_has_correct_name(self):
        self.assertTrue(ValidateBasicData.validate_name(BASIC_INFO_1))

    def test_object_has_incorrect_name_contains_whitespaces(self):
        self.assertFalse(ValidateBasicData.validate_name(BASIC_INFO_2))

    def test_object_has_incorrect_name_contains_numbers(self):
        self.assertFalse(ValidateBasicData.validate_name(BASIC_INFO_3))

    # TESTS Price

    def test_object_has_correct_price(self):
        self.assertTrue(ValidateBasicData.validate_price(BASIC_INFO_1))

    def test_object_has_incorrect_price_contains_float(self):
        self.assertFalse(ValidateBasicData.validate_price(BASIC_INFO_2))

    def test_object_has_incorrect_price_contains_string(self):
        self.assertFalse(ValidateBasicData.validate_price(BASIC_INFO_3))

    def test_object_has_incorrect_price_contains_negative_decimal(self):
        self.assertFalse(ValidateBasicData.validate_price(BASIC_INFO_4))

    # TESTS Mileage

    def test_object_has_correct_mileage(self):
        self.assertTrue(ValidateBasicData.validate_mileage(BASIC_INFO_1))

    def test_object_has_incorrect_mileage_contains_string(self):
        self.assertFalse(ValidateBasicData.validate_mileage(BASIC_INFO_2))

    def test_object_has_incorrect_mileage_contains_negative_value(self):
        self.assertFalse(ValidateBasicData.validate_mileage(BASIC_INFO_3))
