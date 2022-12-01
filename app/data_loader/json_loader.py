from app.model.car import Car
from app.validator.validator import validate_car
import json

# TODO fake file z testowym carem
# TODO sprawdzenie złej ścieżki do file
# TODO sprawdź czy plik jest pusty


def get_cars(filename: str) -> list['Car']:
    with open(filename, 'r') as json_file:
        try:
            json_data = json.load(json_file)
            cars = []
            for data in json_data:
                car = Car.of(data)
                if validate_car(car):
                    cars.append(car)
            return cars
        except Exception as e:
            raise ValueError(e)
