from app.model.car import Car
from statistics import mean
from app.service.types import SortType, Statistics, StatisticsCriteria
from decimal import Decimal


class CarService:
    def __init__(self, cars: list[Car]):
        self.cars = cars

    def __str__(self):
        return f'{self.cars}'

    def get_single_car(self) -> Car:
        return self.cars[0]

    def get_cars_sorted_by_selected_criteria(self, sort_type: SortType, reverse: bool) -> list[Car]:
        match sort_type:
            case sort_type.POWER:
                return sorted([car for car in self.cars], key=lambda x: x.engine.power, reverse=reverse)
            case sort_type.SIZE:
                return sorted([car for car in self.cars], key=lambda x: x.wheel.size, reverse=reverse)
            case _:
                return sorted([car for car in self.cars], key=lambda x: len(x.carBody.components), reverse=reverse)

    def get_cars_sorted_by_model_with_selected_car_body(self, car_body: str, min_price: Decimal, max_price: Decimal) -> list[Car]:
        if min_price > max_price:
            raise ValueError('Price range is not valid')
        return [car for car in self.cars if car.car_body.type == car_body and car.has_price_between(min_price, max_price)]

    def get_cars_sorted_by_model_with_selected_engine(self, engine: str) -> list[Car]:
        return sorted([car for car in self.cars if car.engine.type == engine], key=lambda x: x.engine.power, reverse=True)


    def _get_price_statistics(self) -> Statistics:
        car_prices = [car.price for car in self.cars]
        return Statistics(
            min(car_prices),
            mean(car_prices),
            max(car_prices)
        )

    def _get_mileage_statistics(self) -> Statistics:
        car_mileage = [car.mileage for car in self.cars]
        return Statistics(
            min(car_mileage),
            mean(car_mileage),
            max(car_mileage)
        )

    def _get_power_statistics(self) -> Statistics:
        car_power = [car.engine.power for car in self.cars]
        return Statistics(
            min(car_power),
            mean(car_power),
            max(car_power)
        )

    def get_cars_statistics(self, criteria: StatisticsCriteria) -> Statistics:
        match criteria:
            case StatisticsCriteria.PRICE:
                return self._get_price_statistics()
            case StatisticsCriteria.MILEAGE:
                return self._get_mileage_statistics()
            case StatisticsCriteria.POWER:
                return self._get_power_statistics()

    def get_dict_of_car_mileage(self):
        unsorted_dict_of_cars = {car.model: car.mileage for car in self.cars}
        return dict(sorted(unsorted_dict_of_cars.items(), reverse=True))

    def get_dict_of_tyre_type(self) -> dict[Car]:
        unsorted_dict_of_tyres = {tyre.wheel.type: [car for car in self.cars if car.wheel.type == tyre.wheel.type] for tyre in self.cars}
        return dict(sorted(unsorted_dict_of_tyres.items(), key=lambda item: len(item[1]), reverse=True))

    def get_cars_with_selected_component(self, component: str) -> list[Car]:
        if not isinstance(component, str):
            raise ValueError('Passed value is not a string')
        return sorted([car for car in self.cars if car.has_component(component)], key=lambda x: x.model, reverse=False)

    def get_cars_with_price_between(self, min_price: Decimal, max_price: Decimal) -> list[Car]:
        if min_price > max_price:
            raise ValueError("Speed range is not correct")
        return [car for car in self.cars if car.has_price_between(min_price, max_price)]
