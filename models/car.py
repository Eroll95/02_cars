from dataclasses import dataclass
from enum import Enum, unique


@unique
class EngineType(Enum):
    DIESEL = 1
    GASOLINE = 2
    LPG = 3


@dataclass
class Engine:
    type: EngineType
    power: int

