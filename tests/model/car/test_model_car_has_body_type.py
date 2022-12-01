import unittest
from tests.data import CAR_1
from app.model import CarBodyType

body_types = [body_type for body_type in CarBodyType]


class CarModelHasBodyType(unittest.TestCase):
    def test_has_valid_body_type(self):
        self.assertTrue(CAR_1.car_body.type in body_types)

    def test_has_expected_body_type(self):
        expected_body_type = CarBodyType(1)
        self.assertTrue(CAR_1.car_body.has_body_type(expected_body_type))

    def test_has_invalid_body_type(self):
        self.assertFalse(CAR_1.car_body.type not in body_types)

    def test_has_unexpected_body_type(self):
        expected_body_type = CarBodyType(2)
        self.assertFalse(CAR_1.car_body.has_body_type(expected_body_type))
