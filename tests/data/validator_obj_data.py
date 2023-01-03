from app.validator.validator import ValidateBasicData, ValidateEngineData, ValidateCarBodyData, ValidateWheelData

DATA_INFO_1 = {'model': 'AUDI', 'price': 120, 'mileage': 12000,
               'engine': {'type': 'DIESEL', 'power': 210.0},
               'car_body': {'color': 'BLACK', 'type': 'SEDAN',
                            'components': ['AUTOMATIC TRANSMISSION', 'LED HEADLIGHTS', 'AIR CONDITIONING', 'ALLOY WHEELS','LEATHER SEATS', 'BLUETOOTH']},
               'wheel': {'type': 'SUMMER', 'model': 'BRIDGESTONE', 'size': 18}}

BASIC_INFO_1 = ValidateBasicData(DATA_INFO_1)
ENGINE_INFO_1 = ValidateEngineData(DATA_INFO_1)
BODY_INFO_1 = ValidateCarBodyData(DATA_INFO_1)
WHEEL_INFO_1 = ValidateWheelData(DATA_INFO_1)
