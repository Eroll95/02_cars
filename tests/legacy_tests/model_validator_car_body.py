import unittest
from collections import Counter
from app.validator.validator import validate_color, validate_body_type, validate_components
from tests.data.data import CAR_1, CAR_2, CAR_3, CAR_4


class ValidatorValidateCarBodyData(unittest.TestCase):
    def test_object_has_correct_color(self):
        self.assertTrue(validate_color(CAR_1.car_body))

    def test_object_has_correct_body_type(self):
        self.assertTrue(validate_body_type(CAR_1.car_body))

    # Validate Component list--------------------------------------------------------

    @staticmethod
    def test_object_component_list_has_any_items():
        assert len(CAR_3.car_body.components) > 0

    def test_object_has_correct_component(self):
        self.assertTrue((validate_components(CAR_1.car_body)))

    @staticmethod
    def test_object_component_list_contains_duplicates():
        component_list = [component for component in CAR_3.car_body.components]
        assert len([item for item, count in Counter(component_list).items() if count > 1]) > 0

    def test_object_has_incorrect_component_contains_lower_chars(self):
        self.assertFalse(validate_components(CAR_2.car_body))

    @staticmethod
    def test_object_component_list_is_empty():
        assert len(CAR_4.car_body.components) == 0
