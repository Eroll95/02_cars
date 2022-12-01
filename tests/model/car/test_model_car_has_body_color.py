import unittest
from tests.data import CAR_1
from app.model import CarBodyColor

body_colors = [color for color in CarBodyColor]


class CarModelHasBodyColor(unittest.TestCase):
    def test_has_valid_body_color(self):
        self.assertTrue(CAR_1.car_body.color in body_colors)

    def test_has_expected_body_color(self):
        expected_body_color = CarBodyColor(1)
        self.assertTrue(CAR_1.car_body.has_color(expected_body_color))

    def test_has_invalid_body_color(self):
        self.assertFalse(CAR_1.car_body.color not in body_colors)

    def test_has_unexpected_body_color(self):
        expected_body_color = CarBodyColor(2)
        self.assertFalse(CAR_1.car_body.has_color(expected_body_color))
