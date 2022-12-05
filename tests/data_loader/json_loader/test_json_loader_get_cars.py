import unittest
import pytest
import os
from app.data_loader.json_loader import get_cars
from typing import Final

cars_filename_path: Final[str] = r'C:\Dev\kmprograms\praktyka\praktyka - python\09_OBIEKTY\02_cars\resources\cars.json'

# TODO - ścieżki relatywne


class JsonLoaderImportData(unittest.TestCase):
    def test_load_correct_file(self):
        self.assertTrue(get_cars(cars_filename_path))

    def test_load_one_example_object(self):
        path = r'C:\Dev\kmprograms\praktyka\praktyka - python\09_OBIEKTY\02_cars\tests\test_files\test_car.json'
        self.assertTrue(get_cars(relative_path))

    def test_load_wrong_data_format(self):
        path = r'C:\Dev\kmprograms\praktyka\praktyka - python\09_OBIEKTY\02_cars\tests\test_files\wrong_format.json'
        self.assertRaises(ValueError, lambda: get_cars(path))

    def test_load_empty_file(self):
        path = r'C:\Dev\kmprograms\praktyka\praktyka - python\09_OBIEKTY\02_cars\tests\test_files\empty_file.json'
        self.assertRaises(ValueError, lambda: get_cars(path))

    @pytest.mark.xfail()
    def test_if_file_is_empty(self):
        empty_file_path = r'C:\Dev\kmprograms\praktyka\praktyka - python\09_OBIEKTY\02_cars\tests\test_files\empty_file.json'
        assert os.path.getsize(cars_filename_path) == 0

    @staticmethod
    def test_if_file_is_not_empty():
        assert os.path.getsize(cars_filename_path) > 0
