from app.model.car import Car, CarBody, CarBodyType, CarBodyColor, Engine, EngineType, Wheel, TyreType
from app.validator.validator import ValidateBasicData, ValidateEngineData, ValidateCarBodyData, ValidateWheelData
from decimal import Decimal


CAR_BODY_1 = CarBody(CarBodyColor(1), CarBodyType(1), components=['LED HEADLIGHTS'])
ENGINE_1 = Engine(EngineType(1), 150.0)
WHEEL_1 = Wheel(TyreType(1), 'PIRELLI', 17)
CAR_1 = Car('AUDI', Decimal('100'), 2000, ENGINE_1, CAR_BODY_1, WHEEL_1)

CAR_BODY_2 = CarBody(CarBodyColor(2), CarBodyType(2), components=['LED HEADLIGHTS', 'led'])
ENGINE_2 = Engine(EngineType(2), 150)
WHEEL_2 = Wheel(TyreType(2), 'PIRELLI3', -18)
CAR_2 = Car('ALFA ROMEO', 200, '2000', ENGINE_2, CAR_BODY_2, WHEEL_2)

CAR_BODY_3 = CarBody(CarBodyColor(2), CarBodyType(2), components=['BLUETOOTH', 'BLUETOOTH'])
ENGINE_3 = Engine(EngineType(2), '150.0')
WHEEL_3 = Wheel(TyreType(2), 'pirelli', 18)
CAR_3 = Car('BM3W', '150', -2000, ENGINE_3, CAR_BODY_3, WHEEL_3)

CAR_BODY_4 = CarBody(CarBodyColor(2), CarBodyType(2), components=[])
ENGINE_4 = Engine(EngineType(2), -150.0)
WHEEL_4 = Wheel(TyreType(2), 'PIR@ELLI', 18)
CAR_4 = Car('MERCEDES', Decimal('-200'), 2000, ENGINE_4, CAR_BODY_4, WHEEL_4)

DATA_INFO_1 = {'model': 'AUDI', 'price': 120, 'mileage': 12000,
               'engine': {'type': 'DIESEL', 'power': 210.0},
               'car_body': {'color': 'BLACK', 'type': 'SEDAN',
                            'components': ['AUTOMATIC TRANSMISSION', 'LED HEADLIGHTS', 'AIR CONDITIONING', 'ALLOY WHEELS','LEATHER SEATS', 'BLUETOOTH']},
               'wheel': {'type': 'SUMMER', 'model': 'BRIDGESTONE', 'size': 18}}

BASIC_INFO_1 = ValidateBasicData(DATA_INFO_1)
ENGINE_INFO_1 = ValidateEngineData(DATA_INFO_1)
BODY_INFO_1 = ValidateCarBodyData(DATA_INFO_1)
WHEEL_INFO_1 = ValidateWheelData(DATA_INFO_1)
