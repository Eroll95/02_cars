from dataclasses import dataclass
from enum import Enum, unique


@unique
class EngineType(Enum):
    DIESEL = 1
    GASOLINE = 2
    LPG = 3


@unique
class TyreType(Enum):
    WINTER = 1
    SUMMER = 2


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


@dataclass
class Engine:
    type: EngineType
    power: int


@dataclass
class Wheel:
    model: str
    size: int
    type: TyreType


@dataclass
class CarBody:
    color: CarBodyColor
    type: CarBodyType
    components: list[str]


@dataclass
class Car:
    model: str
    price: int
    mileage: int
    engine: Engine
    carBody: CarBody
    wheel: Wheel
