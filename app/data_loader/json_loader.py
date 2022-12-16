from app.model.car import Car
# from app.validator.validator import validate_car
from app.validator.validator import ValidateBasicData, ValidateWheelData, ValidateCarBodyData, ValidateEngineData
import json
from typing import Final, Any


def get_cars(filename: str) -> [dict[str, Any]]:
    with open(filename, 'r') as json_file:
        try:
            json_data = json.load(json_file)
            cars = []
            for data in json_data:
                car_basic_info = ValidateBasicData(data)
                car_engine_info = ValidateEngineData(data)
                car_body_info = ValidateCarBodyData(data)
                car_wheel_info = ValidateWheelData(data)
                if car_basic_info.validate_basic_data():
                    car = Car.of(data)
                    cars.append(car)
            return cars
        except Exception as e:
            raise ValueError(e)


if __name__ == '__main__':
    cars_main_filename_path: Final[str] = r'.\..\resources\cars.json'
    cars_testfile_path: Final[str] = r'.\..\..\tests\test_files\test_car.json'
    car1 = get_cars(cars_main_filename_path)
    print(car1)

