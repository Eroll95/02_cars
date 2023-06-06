import pytest
import unittest
from tests.data.validator_obj_data import ENGINE_INFO_1, ENGINE_INFO_2, ENGINE_INFO_3, ENGINE_INFO_4
from app.validator.validator import ValidateEngineData


class ValidatorValidateEngineData(unittest.TestCase):

    def test_object_has_expected_engine_type(self):
        self.assertTrue(ValidateEngineData.validate_engine_type(ENGINE_INFO_1))

    # def test_object_has_unexpected_engine_type(self):
    #      self.assertTrue(ValidateEngineData.validate_engine_type(ENGINE_INFO_2))

    def test_object_has_correctly_spelled_engine_type(self):
        self.assertTrue(ValidateEngineData.validate_engine_type(ENGINE_INFO_1))

    def test_object_has_incorrect_spelled_engine_type(self):
        self.assertFalse(ValidateEngineData.validate_engine_type(ENGINE_INFO_2))
        # self.assertRaises(ValueError, lambda: ValidateEngineData.validate_engine_type(ENGINE_INFO_2))

    # TEST Engine power---------------------------------------------------------

    def test_object_has_correct_engine_power(self):
        self.assertTrue(ValidateEngineData.validate_engine_power(ENGINE_INFO_1))

    def test_object_has_incorrect_engine_power_value_contains_integer(self):
        self.assertFalse(ValidateEngineData.validate_engine_power(ENGINE_INFO_2))

    def test_object_has_incorrect_engine_power_value_is_negative(self):
        self.assertFalse(ValidateEngineData.validate_engine_power(ENGINE_INFO_3))

    def test_object_has_incorrect_engine_power_value_contains_string(self):
        self.assertFalse(ValidateEngineData.validate_engine_power(ENGINE_INFO_4))
