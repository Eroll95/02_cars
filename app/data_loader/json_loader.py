from app.model.car import Car
# from app.validator.validator import validate_car
from app.validator.validator import ValidateWheelData
from app.validator.validator import ValidateBasicData
import json
from typing import Final, Any

# LEGACY - for validating object models instead of dict from json


# def get_cars_legacy(filename: str) -> list['Car']:
#     with open(filename, 'r') as json_file:
#         try:
#             json_data = json.load(json_file)
#             cars = []
#             for data in json_data:
#                 car = Car.of(data)
#                 if validate_car(car):
#                     cars.append(car)
#             return cars
#         except Exception as e:
#             raise ValueError(e)


def get_cars(filename: str) -> [dict[str, Any]]:
    with open(filename, 'r') as json_file:
        try:
            json_data = json.load(json_file)
            cars = []
            for data in json_data:
                car = ValidateWheelData(data)
                if car.validate_wheel():
                    car = Car.of(data)
                    cars.append(car)
            return cars
        except Exception as e:
            raise ValueError(e)


if __name__ == '__main__':
    cars_staging_filename_path: Final[str] = r'.\..\resources\cars.json'
    cars_dev_testfile_path: Final[str] = r'.\..\..\tests\test_files\test_car.json'
    car1 = get_cars(cars_dev_testfile_path)

    print(type(car1[0]))
