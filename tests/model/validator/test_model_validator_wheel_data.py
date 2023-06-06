import pytest
import unittest
from tests.data.validator_obj_data import WHEEL_INFO_1, WHEEL_INFO_2, WHEEL_INFO_3, WHEEL_INFO_4, WHEEL_INFO_5
from app.validator.validator import ValidateWheelData


class ValidatorValidateCarWheelData(unittest.TestCase):

    # TEST Wheel type---------------------------------------------------------

    def test_object_has_correct_wheel_type(self):
        self.assertTrue(ValidateWheelData.validate_type(WHEEL_INFO_1))

    def test_object_has_incorrect_wheel_type_contains_lower_chars(self):
        self.assertFalse(ValidateWheelData.validate_model(WHEEL_INFO_2))

    def test_object_has_incorrect_wheel_type_contains_numbers(self):
        self.assertFalse(ValidateWheelData.validate_model(WHEEL_INFO_3))

    def test_object_has_incorrect_wheel_type_contains_invalid_chars(self):
        self.assertFalse(ValidateWheelData.validate_model(WHEEL_INFO_4))

    # TEST Wheel Name---------------------------------------------------------

    def test_object_has_correct_wheel_name(self):
        self.assertTrue(ValidateWheelData.validate_model(WHEEL_INFO_1))

    def test_object_has_incorrect_wheel_model_name_contains_lower_chars(self):
        self.assertFalse(ValidateWheelData.validate_model(WHEEL_INFO_2))

    def test_object_has_incorrect_wheel_model_name_contains_numbers(self):
        self.assertFalse(ValidateWheelData.validate_model(WHEEL_INFO_3))

    def test_object_has_incorrect_wheel_model_name_contains_invalid_chars(self):
        self.assertFalse(ValidateWheelData.validate_model(WHEEL_INFO_4))

    # TEST Wheel size---------------------------------------------------------

    def test_object_has_correct_wheel_size(self):
        self.assertTrue(ValidateWheelData.validate_size(WHEEL_INFO_1))

    def test_object_has_incorrect_wheel_size_contains_negative_value(self):
        self.assertFalse(ValidateWheelData.validate_size(WHEEL_INFO_2))

    def test_object_has_incorrect_wheel_size_contains_zero_value(self):
        self.assertFalse(ValidateWheelData.validate_size(WHEEL_INFO_3))

    def test_object_has_incorrect_wheel_size_contains_no_value(self):
        self.assertFalse(ValidateWheelData.validate_size(WHEEL_INFO_5))
