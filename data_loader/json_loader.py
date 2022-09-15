from models.car import Car, Engine, CarBody, Wheel
import json


def get_cars(filename: str) -> list['Car']:
    with open(filename, 'r') as json_file:
        try:
            json_data = json.load(json_file)
        except Exception as e:
            print(e)

        return [Car(row['model'], row['price'], row['mileage'],
                   Engine(row['engine']['type'], row['engine']['power']),
                   CarBody(row['carBody']['color'], row['carBody']['type'], row['carBody']['components']),
                   Wheel(row['wheel']['type'], row['wheel']['model'], row['wheel']['size'])) for row in json_data]
