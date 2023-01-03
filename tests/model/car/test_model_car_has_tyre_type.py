import unittest
from tests.data.car_obj_data import CAR_1
from app.model.car import TyreType

tyre_types = [tyre for tyre in TyreType]


class CarModelHasTyreType(unittest.TestCase):
    def test_has_valid_engine_type(self):
        self.assertTrue(CAR_1.wheel.type in tyre_types)

    def test_has_expected_engine_type(self):
        expected_tyre_type = TyreType(1)
        self.assertTrue(CAR_1.wheel.has_tyre_type(expected_tyre_type))

    def test_has_invalid_engine_type(self):
        self.assertFalse(CAR_1.wheel.type not in tyre_types)

    def test_has_unexpected_engine_type(self):
        expected_tyre_type = TyreType(2)
        self.assertFalse(CAR_1.wheel.has_tyre_type(expected_tyre_type))
