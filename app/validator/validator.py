from app.validator.basic_validator import matches_regex, value_in_between_range
from app.model.car import *
from decimal import Decimal
from dataclasses import dataclass
from typing import Final, Any
from collections import Counter
import logging
import re

logging.basicConfig(level=logging.INFO)

PRICE_MAX: Final[Decimal] = Decimal('1000000')
MILEAGE_MAX: Final[int] = 1000000

# TODO - walidacja na poziomie dict nie na poziomie obiektu
# TODO - podzielić walidatory na klasy


# def validate_car(car: Car) -> bool:
#     return validate_basic_data(car) and validate_engine(car.engine) and validate_car_body(car.car_body) and validate_wheel(car.wheel)
#
#
# def validate_basic_data(car: Car) -> bool:
#     return validate_name(car) and validate_price(car) and validate_mileage(car)
#
#
# def validate_name(car: Car) -> bool:
#     return matches_regex(r'^[A-Z]+$', car.model)
#
#
# def validate_price(car: Car) -> bool:
#     return isinstance(car.price, Decimal) and value_in_between_range(0, PRICE_MAX, car.price)
#
#
# def validate_mileage(car: Car) -> bool:
#     return isinstance(car.mileage, int) and value_in_between_range(0, MILEAGE_MAX, car.mileage)
#
#
# # Validate Engine---------------------------------------------------
#
# def validate_engine(engine: Engine) -> bool:
#     return validate_engine_type(engine) and validate_engine_power(engine)
#
#
# def validate_engine_type(engine: Engine) -> bool:
#     return matches_regex(r'^[A-Z]+$', engine.type.name)
#
#
# def validate_engine_power(engine: Engine) -> bool:
#     return isinstance(engine.power, float) and value_in_between_range(0, 10000, engine.power)
#
#
# # Validate CarBody--------------------------------------------------
#
# def validate_car_body(car_body: CarBody) -> bool:
#     return validate_color(car_body) and validate_body_type(car_body) and validate_components(car_body)
#
#
# def validate_color(car_body: CarBody) -> bool:
#     return matches_regex(r'^[A-Z]+$', car_body.color.name)
#
#
# def validate_body_type(car_body: CarBody) -> bool:
#     return matches_regex(r'^[A-Z]+$', car_body.type.name)
#
#
# def validate_components(car_body: CarBody) -> bool:
#     if False in [item.isupper() for item in car_body.components]:
#         return False
#     if len([item for item, count in Counter(car_body.components).items() if count > 1]) > 0:
#         return False
#     return True
#
#
# def validate_wheel(wheel: Wheel) -> bool:
#     return validate_wheel_type(wheel) and validate_model(wheel) and validate_size(wheel)
#
#
# def validate_wheel_type(wheel: Wheel) -> bool:
#     return matches_regex(r'^[A-Z]+$', wheel.type.name)
#
#
# def validate_model(wheel: Wheel) -> bool:
#     return matches_regex(r'^[A-Z]+$', wheel.model)
#
#
# def validate_size(wheel: Wheel) -> bool:
#     return isinstance(wheel.size, int) and wheel.size > 0

# Validate Basic Info--------------------------------------------------------

class ValidateBasicData:
    def __init__(self, data: dict[str, Any]):
        self.data = data
# def validate_basic_data(car: Car) -> bool:
#     return validate_name(car) and validate_price(car) and validate_mileage(car)
#
#
# def validate_name(car: Car) -> bool:
#     return matches_regex(r'^[A-Z]+$', car.model)
#
#
# def validate_price(car: Car) -> bool:
#     return isinstance(car.price, Decimal) and value_in_between_range(0, PRICE_MAX, car.price)
#
#
# def validate_mileage(car: Car) -> bool:
#     return isinstance(car.mileage, int) and value_in_between_range(0, MILEAGE_MAX, car.mileage)

# Validate Wheel--------------------------------------------------------


class ValidateWheelData:
    def __init__(self, data: dict[str, Any]):
        self.data = data

    def __str__(self):
        return f'{self.data}'

    def validate_wheel(self) -> bool:
        return self.validate_wheel_type() and self.validate_model() and self.validate_size()

    def validate_wheel_type(self) -> bool:
        return matches_regex(r'^[A-Z]+$', self.data['wheel']['type'])

    def validate_model(self) -> bool:
        return matches_regex(r'^[A-Z]+$', self.data['wheel']['model'])

    def validate_size(self) -> bool:
        return isinstance(self.data['wheel']['size'], int) and self.data['wheel']['size'] > 0
