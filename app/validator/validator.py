from app.validator.basic_validator import matches_regex, value_in_between_range
from app.model.car import *
from decimal import Decimal
from dataclasses import dataclass
from typing import Final, Any
from collections import Counter


PRICE_MAX: Final[Decimal] = Decimal('1000000')
MILEAGE_MAX: Final[int] = 1000000

# TODO - walidacja na poziomie dict nie na poziomie obiektu
# TODO - podzielić walidatory na klasy


@dataclass
class ValidateBasicData:
    data: dict[str, Any]

    def validate_basic_data(self) -> bool:
        return self.validate_name() and self.validate_price() and self.validate_mileage()

    def validate_name(self) -> bool:
        return matches_regex(r'^[A-Z]+$', self.data['model'])

    def validate_price(self) -> bool:
        return isinstance(self.data['price'], Decimal) and value_in_between_range(0, PRICE_MAX, self.data['price'])

    def validate_mileage(self) -> bool:
        return isinstance(self.data['mileage'], int) and value_in_between_range(0, MILEAGE_MAX, self.data['mileage'])


@dataclass
class ValidateEngineData:
    data: dict[str, Any]

    def validate_engine(self) -> bool:
        return self.validate_engine_type() and self.validate_engine_power()

    def validate_engine_type(self) -> bool:
        return matches_regex(r'^[A-Z]+$', self.data['engine']['type'])

    def validate_engine_power(self) -> bool:
        return isinstance(self.data['engine']['power'], float) and value_in_between_range(0, 10000, self.data['engine']['power'])


@dataclass
class ValidateCarBodyData:
    data: dict[str, Any]

    def validate_car_body(self) -> bool:
        return self.validate_color() and self.validate_body_type() and self.validate_components()

    def validate_color(self) -> bool:
        return matches_regex(r'^[A-Z]+$', self.data['car_body']['color'])

    def validate_body_type(self) -> bool:
        return matches_regex(r'^[A-Z]+$', self.data['car_body']['type'])

    def validate_components(self) -> bool:
        if False in [item.isupper() for item in self.data['car_body']['components']]:
            return False
        if len([item for item, count in Counter(self.data['car_body']['components']).items() if count > 1]) > 0:
            return False
        return True


@dataclass
class ValidateWheelData:
    data: dict[str, Any]

    def validate_wheel(self) -> bool:
        return self.validate_wheel_type() and self.validate_model() and self.validate_size()

    def validate_wheel_type(self) -> bool:
        return matches_regex(r'^[A-Z]+$', self.data['wheel']['type'])

    def validate_model(self) -> bool:
        return matches_regex(r'^[A-Z]+$', self.data['wheel']['model'])

    def validate_size(self) -> bool:
        return isinstance(self.data['wheel']['size'], int) and self.data['wheel']['size'] > 0

