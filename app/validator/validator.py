from app.validator.basic_validator import matches_regex, value_in_between_range
from app.model.car import *
from decimal import Decimal
from dataclasses import dataclass
from typing import Final, Any


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
