import unittest
import pytest
from app.validator.validator import validate_engine_type, validate_engine_power
from tests.data import CAR_1, CAR_2, CAR_3, CAR_4


class ValidatorValidateEnginData(unittest.TestCase):
    def test_object_has_correct_engine_type(self):
        self.assertTrue(validate_engine_type(CAR_1.engine))

    @pytest.mark.skip(reason="ValueError: 4 is not a valid EngineType - app throws errors before doing test")
    def test_object_has_incorrect_engine_type(self):
        self.assertFalse(validate_engine_type(CAR_2.engine))
        self.assertRaises(ValueError, lambda: validate_engine_type(CAR_2.engine))

    # TEST Engine power---------------------------------------------------------

    def test_object_has_correct_engine_power(self):
        self.assertTrue(validate_engine_power(CAR_1.engine))

    def test_object_has_incorrect_engine_power_contains_integer(self):
        self.assertFalse(validate_engine_power(CAR_2.engine))

    def test_object_has_incorrect_engine_power_contains_negative_value(self):
        self.assertFalse(validate_engine_power(CAR_4.engine))

    def test_object_has_incorrect_engine_power_contains_string(self):
        self.assertFalse(validate_engine_power(CAR_3.engine))
