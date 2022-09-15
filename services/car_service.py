import json
from models.car import Car
from data_loader.json_loader import get_cars
from models.validator import validate_car
from statistics import mean
from services.types import SortType
from decimal import Decimal
import operator


class CarService:
    def __init__(self, filename: str):
        self.cars = [car for car in get_cars(filename) if validate_car(car)]

    def __str__(self):
        return f'{self.cars}'

    def get_first_one(self):
        return self.cars[0].has_price_between(150, 260)

    def get_cars_sorted_by_selected_criteria(self, sort_type: SortType, reverse: bool) -> list['Car']:
        match sort_type:
            case sort_type.POWER:
                return sorted([car for car in self.cars], key=lambda x: x.engine.power, reverse=reverse)
            case sort_type.SIZE:
                return sorted([car for car in self.cars], key=lambda x: x.wheel.size, reverse=reverse)
            case sort_type.COMPONENTS:
                return sorted([car for car in self.cars], key=lambda x: len(x.carBody.components), reverse=reverse)
            case _:
                pass

    def get_cars_sorted_by_model_with_selected_car_body(self, car_body: str, min_v: int, max_v: int) -> list['Car']:
        if min_v > max_v:
            raise ValueError('Price range is not valid')
        return [car for car in self.cars if car.carBody.type == car_body and (min_v <= car.price <= max_v)]

    def get_cars_sorted_by_model_with_selected_engine(self, engine: str) -> list['Car']:
        return sorted([car for car in self.cars if car.engine.type == engine], key=lambda x: x.engine.power,
                      reverse=True)

    #Można spróbować w klasie Car ogarnąć to
    def get_cars_statistics(self, criteria: str) -> str:
        car_prices = [row.price for row in self.cars]
        car_mileage = [row.mileage for row in self.cars]
        car_power = [row.engine.power for row in self.cars]
        match criteria:
            case 'price':
                return f'''
                    Car statistics:
        
                    Most expensive car: {max(car_prices)}
                    Cheapest car: {min(car_prices)}
                    Average car price: {round(mean(car_prices), 2)}
                    '''
            case 'mileage':
                return f'''
                    Car statistics:
        
                    Highest mileage: {max(car_mileage)}
                    Lowest mileage: {min(car_mileage)}
                    Average mileage: {round(mean(car_mileage), 2)}
                    '''
            case 'power':
                return f'''
                    Car statistics:
                    
                    Highest engine power: {max(car_power)}
                    Lowest engine power: {min(car_power)}
                    Average engine power: {round(mean(car_power), 2)}
                    '''

    #TODO dokonczyc:
    def get_dict_of_car_mileage(self):
        return {row.model: row.mileage for row in self.cars}

    def get_dict_of_tyre_type(self) -> dict['Car']:
        l1 = {row.wheel.type: [c for c in self.cars if c.wheel.type == row.wheel.type]
              for row in self.cars}
        # return l1
        return dict(sorted(l1.items(), key=lambda item: len(item[1]), reverse=True))

    def get_cars_with_selected_component(self, component: str) -> list['Car']:
        return sorted([row for row in self.cars if component in row.carBody.components], key=lambda x: x.model,
                      reverse=False)
