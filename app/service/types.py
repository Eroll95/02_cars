from enum import Enum, unique
from decimal import Decimal
from dataclasses import dataclass

@unique
class SortType(Enum):
    POWER = 0
    SIZE = 1
    COMPONENTS = 2

@dataclass
class Statistics:
    min_value: Decimal | float
    avg_value: Decimal | float
    max_value: Decimal | float

class StatisticsCriteria(Enum):
    MILEAGE = 1,
    POWER = 2,
    PRICE = 3

