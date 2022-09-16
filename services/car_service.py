from models.car import Car
from data_loader.json_loader import get_cars
from models.validator import validate_car
from statistics import mean
from services.types import SortType
from decimal import Decimal


class CarService:
    def __init__(self, filename: str):
        self.cars = [car for car in get_cars(filename) if validate_car(car)]

    def __str__(self):
        return f'{self.cars}'

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

    def get_cars_sorted_by_model_with_selected_car_body(self, car_body: str, min_price: Decimal, max_price: Decimal) -> list['Car']:
        if min_price > max_price:
            raise ValueError('Price range is not valid')
        return [car for car in self.cars if car.carBody.type == car_body and car.has_price_between(min_price, max_price)]

    def get_cars_sorted_by_model_with_selected_engine(self, engine: str) -> list['Car']:
        return sorted([car for car in self.cars if car.engine.type == engine], key=lambda x: x.engine.power, reverse=True)

    #Można spróbować w klasie Car ogarnąć to
    def get_cars_statistics(self, criteria: str) -> str:
        car_prices = [car.price for car in self.cars]
        car_mileage = [car.mileage for car in self.cars]
        car_power = [car.engine.power for car in self.cars]
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

    #TODO if key = car unhashable:
    def get_dict_of_car_mileage(self):
        unsorted_dict_of_cars = {car.model: car.mileage for car in self.cars}
        return dict(sorted(unsorted_dict_of_cars.items(), reverse=True))

    def get_dict_of_tyre_type(self) -> dict['Car']:
        unsorted_dict_of_tyres = {tyre.wheel.type: [car for car in self.cars if car.wheel.type == tyre.wheel.type] for tyre in self.cars}
        return dict(sorted(unsorted_dict_of_tyres.items(), key=lambda item: len(item[1]), reverse=True))

    def get_cars_with_selected_component(self, component: str) -> list['Car']:
        if not isinstance(component, str):
            raise ValueError('Passed value is not a string')
        return sorted([car for car in self.cars if car.has_component(component)], key=lambda x: x.model, reverse=False)
