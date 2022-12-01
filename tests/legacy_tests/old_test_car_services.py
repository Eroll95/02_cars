import unittest
from app.service import car_service
from app.data_loader.json_loader import get_cars
from app.service.types import SortType
from typing import Final
from decimal import Decimal


class TestCarService(unittest.TestCase):

    def setUp(self) -> None:
        cars_filename: Final = r'resources\cars.json'
        self.cars = car_service.CarService(get_cars(cars_filename))

    def test_get_cars_sorted_by_criteria(self):
        self.assertEqual(5, len(self.cars.get_cars_sorted_by_selected_criteria(SortType.SIZE, False)))

    @unittest.skip('Test not finished')
    def test_get_dict_of_tyre_type(self):
        pass

    def test_get_cars_with_selected_component(self):
        self.assertEqual(3, len(self.cars.get_cars_with_selected_component(component='SPORT PACKAGE')))

    def test_cars_with_price_between(self):
        self.assertNotEqual(3, len(self.cars.get_cars_with_price_between(Decimal(100), Decimal(250))))


if __name__ == '__main__':
    unittest.main()
