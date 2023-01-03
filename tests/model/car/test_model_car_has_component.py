import unittest
from tests.data.car_obj_data import CAR_1


class CarModelHasComponent(unittest.TestCase):
    def test_has_component(self):
        expected_component = 'LED HEADLIGHTS'
        self.assertTrue(CAR_1.has_component(expected_component))

    def test_no_component(self):
        expected_component = 'LED'
        self.assertFalse(CAR_1.has_component(expected_component))
