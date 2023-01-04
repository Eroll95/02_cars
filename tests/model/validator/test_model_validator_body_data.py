import pytest
import unittest
from tests.data.validator_obj_data import BODY_INFO_1, BODY_INFO_2, BODY_INFO_3, BODY_INFO_4, BODY_INFO_5
from app.validator.validator import ValidateCarBodyData
from collections import Counter


class ValidatorValidateCarBodyData(unittest.TestCase):

    def test_object_has_correct_color(self):
        self.assertTrue(ValidateCarBodyData.validate_color(BODY_INFO_1))

    def test_object_has_incorrect_color_contains_lower_chars(self):
        self.assertFalse(ValidateCarBodyData.validate_color(BODY_INFO_2))

    def test_object_has_correct_body_type(self):
        self.assertTrue(ValidateCarBodyData.validate_color(BODY_INFO_1))

    def test_object_has_incorrect_body_type_contains_lower_chars(self):
        self.assertFalse(ValidateCarBodyData.validate_color(BODY_INFO_2))

        # Validate Component list--------------------------------------------------------

    def test_object_has_correct_components(self):
        self.assertTrue(ValidateCarBodyData.validate_components(BODY_INFO_1))

    def test_object_component_list_contains_duplicates(self):
        self.assertFalse(ValidateCarBodyData.validate_components(BODY_INFO_3))

    def test_object_has_incorrect_component_contains_lower_chars(self):
        self.assertFalse(ValidateCarBodyData.validate_components(BODY_INFO_2))


    # def test_object_component_list_has_any_items(self):
    #     assert len(BODY_INFO_3.data['car_body']['components']) > 0
    #
    # def test_object_component_list_is_empty(self):
    #     assert len(BODY_INFO_4.data['car_body']['components']) == 0
