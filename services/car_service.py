import json
from models.car import Car, CarBodyColor, Engine, EngineType, TyreType, CarBodyType, CarBody, Wheel


class CarService:
    def __init__(self, filename: str):
        with open(filename) as json_file:
            try:
                self.data = json.load(json_file)
            except Exception as e:
                print(e)

        self.cars = [Car(row['model'], row['price'], row['mileage'],
                     Engine(EngineType(row['engine']['type']), row['engine']['power']),
                     CarBody(CarBodyColor(row['carBody']['color']), row['carBody']['type'], row['carBody']['components']),
                     Wheel(TyreType(row['wheel']['type']), row['wheel']['model'], row['wheel']['size'])) for row in self.data]
        # self.cars = [Car(row['model'], row['price'], row['mileage'], Engine(row['engine'], row['engine']),
        #                  CarBody(row['carBody'], row['carBody'], row['carBody'])) for row in self.data]

    # return [Car(row['model'], row['price'], row['mileage'], Color(row['color']), row['components'])
    #         for row in validated_cars]

    @staticmethod
    def _validate_data(data_to_validate):
        pass

    def __str__(self):
        return f'{self.cars}'

    def print_obj(self):
        return f'{self.cars[0].carBody.color}, {self.cars[0].engine.type.name}, {self.cars[0].wheel.type.name}'
