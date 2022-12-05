import unittest
from tests.data import CAR_1
from app.model.car import EngineType

engine_types = [engine for engine in EngineType]


class CarModelHasEngineType(unittest.TestCase):
    def test_has_valid_engine_type(self):
        self.assertTrue(CAR_1.engine.type in engine_types)

    def test_has_expected_engine_type(self):
        expected_engine_type = EngineType(1)
        self.assertTrue(CAR_1.engine.has_engine_type(expected_engine_type))

    def test_has_invalid_engine_type(self):
        self.assertFalse(CAR_1.engine.type not in engine_types)

    def test_has_unexpected_engine_type(self):
        expected_engine_type = EngineType(2)
        self.assertFalse(CAR_1.engine.has_engine_type(expected_engine_type))
