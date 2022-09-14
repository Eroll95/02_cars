from enum import Enum, unique


@unique
class SortType(Enum):
    POWER = 0
    SIZE = 1
    COMPONENTS = 2
