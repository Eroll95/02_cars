import re
from decimal import Decimal
from app.model.car import TyreType
from enum import Enum


def matches_regex(regex_pattern: str, text: str) -> bool:
    return re.match(regex_pattern, text) is not None


def value_in_between_range(min_range: int | Decimal | float,
                           max_range: int | Decimal | float,
                           value: int | Decimal | float) -> bool | ValueError:
    if min_range < max_range:
        return min_range < value < max_range
    raise ValueError('Min value is greater than max value')


def is_value_of(class_type: [Enum], value: str) -> bool:
    return value in [str(enm.name) for enm in class_type]


if __name__ == '__main__':
    if is_value_of(TyreType, 'WINTER'):
        print('Yes')

