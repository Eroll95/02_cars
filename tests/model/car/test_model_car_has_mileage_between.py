import unittest
from tests.data.car_obj_data import CAR_1


class CarModelHasMileageBetween(unittest.TestCase):
    def test_when_mileage_is_in_range(self):
        min_mileage = 10
        max_mileage = 100000
        self.assertTrue(CAR_1.has_mileage_between(min_mileage, max_mileage))

    def test_when_mileage_is_not_in_range(self):
        min_mileage = 100001
        max_mileage = 1000000
        self.assertFalse(CAR_1.has_mileage_between(min_mileage, max_mileage))
