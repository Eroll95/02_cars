import unittest
from app.validator.validator import validate_wheel_type, validate_model, validate_size
from tests.data import CAR_1, CAR_2, CAR_3, CAR_4


class ValidatorValidateCarWheelData(unittest.TestCase):
    def test_object_has_correct_wheel_type(self):
        self.assertTrue(validate_wheel_type(CAR_1.wheel))

    def test_object_has_correct_wheel_model_name(self):
        self.assertTrue(validate_model(CAR_1.wheel))

    # TEST Wheel Name-----------------------------------------------------------------

    def test_object_has_incorrect_wheel_model_name_contains_lower_chars(self):
        self.assertFalse(validate_model(CAR_3.wheel))

    def test_object_has_incorrect_wheel_model_name_contains_numbers(self):
        self.assertFalse(validate_model(CAR_2.wheel))

    def test_object_has_incorrect_wheel_model_name_contains_invalid_chars(self):
        self.assertFalse(validate_model(CAR_4.wheel))

    # TEST Wheel size-----------------------------------------------------------------

    def test_object_has_correct_wheel_size(self):
        self.assertTrue(validate_size(CAR_1.wheel))

    def test_object_has_incorrect_wheel_size_contains_negative_value(self):
        self.assertFalse(validate_size(CAR_2.wheel))
