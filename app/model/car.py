from dataclasses import dataclass
from enum import Enum, unique
from decimal import Decimal
from typing import Any


@unique
class EngineType(Enum):
    DIESEL = 1
    GASOLINE = 2
    LPG = 3


@unique
class CarBodyColor(Enum):
    BLACK = 1
    SILVER = 2
    WHITE = 3
    RED = 4
    BLUE = 5
    GREEN = 6


@unique
class CarBodyType(Enum):
    SEDAN = 1
    HATCHBACK = 2
    ESTATE = 3


@unique
class TyreType(Enum):
    WINTER = 1
    SUMMER = 2


@unique
class TyreModel(Enum):
    BRIDGESTONE = 1
    PIRELLI = 2
    CONTINENTAL = 3


@dataclass(frozen=True)
class Engine:
    type: EngineType
    power: float

    def has_engine_type(self, car_engine_type: EngineType):
        return self.type == car_engine_type

    def has_power_between(self, min_power: float, max_power: float) -> bool:
        return min_power < self.power < max_power

    @classmethod
    def of(cls, data: dict[str, Any]) -> 'Engine':
        return Engine(
            type=EngineType[data['type']],
            power=data['power'])


@dataclass(frozen=True)
class Wheel:
    type: TyreType
    model: str
    size: int

    def has_tyre_type(self, car_tyre_type: TyreType):
        return self.type == car_tyre_type

    @classmethod
    def of(cls, data: dict[str, Any]) -> 'Wheel':
        return Wheel(
            type=TyreType[data['type']],
            model=data['model'],
            size=int(data['size'])
        )


@dataclass(frozen=True)
class CarBody:
    color: CarBodyColor
    type: CarBodyType
    components: list[str]

    def has_color(self, car_body_color: CarBodyColor):
        return self.color == car_body_color

    def has_body_type(self, car_body_type: CarBodyType):
        return self.type == car_body_type

    @classmethod
    def of(cls, data: dict[str, Any]) -> 'CarBody':
        return CarBody(
            color=CarBodyColor[data['color']],
            type=CarBodyType[data['type']],
            components=data['components']
        )


@dataclass(frozen=True)
class Car:
    model: str
    price: Decimal
    mileage: int
    engine: Engine
    car_body: CarBody
    wheel: Wheel

    def has_mileage_between(self, min_mileage: int, max_mileage: int) -> bool:
        return min_mileage < self.mileage < max_mileage

    def has_price_between(self, min_price: Decimal, max_price: Decimal) -> bool:
        return min_price < self.price < max_price

    def has_component(self, component: str) -> bool:
        return component in self.car_body.components

    @classmethod
    def of(cls, data: dict[str, Any]) -> 'Car':
        return Car(
            model=data['model'],
            price=Decimal(data['price']),
            mileage=int(data['mileage']),
            engine=Engine.of(data['engine']),
            car_body=CarBody.of(data['car_body']),
            wheel=Wheel.of(data['wheel'])
        )
