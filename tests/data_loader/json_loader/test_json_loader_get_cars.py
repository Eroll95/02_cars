import unittest
import pytest
import os
from app.data_loader.json_loader import get_cars
from typing import Final

cars_filename_path: Final[str] = r'app\resources\cars.json'

class JsonLoaderImportData(unittest.TestCase):
    def test_load_correct_file(self):
        self.assertTrue(get_cars(cars_filename_path))

    def test_load_one_example_object(self):
        test_car_path = r'.\tests\test_files\test_car.json'
        self.assertTrue(get_cars(test_car_path))

    def test_load_wrong_data_format(self):
        path = r'.\tests\test_files\wrong_format.json'
        self.assertRaises(ValueError, lambda: get_cars(path))

    def test_load_empty_file_throw_value_error(self):
        empty_file_path = r'.\tests\test_files\empty_file.json'
        self.assertRaises(ValueError, lambda: get_cars(empty_file_path))

    @pytest.mark.xfail()
    def test_if_file_is_empty(self):
        empty_file_path = r'.\tests\test_files\empty_file.json'
        assert os.path.getsize(cars_filename_path) == 0

    @staticmethod
    def test_if_file_is_not_empty():
        assert os.path.getsize(cars_filename_path) > 0
