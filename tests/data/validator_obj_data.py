from app.validator.validator import ValidateBasicData, ValidateEngineData, ValidateCarBodyData, ValidateWheelData


BASIC_INFO_1 = ValidateBasicData({'model': 'AUDI', 'price': 120, 'mileage': 12000})
ENGINE_INFO_1 = ValidateEngineData({'engine': {'type': 'DIESEL', 'power': 210.0}})
BODY_INFO_1 = ValidateCarBodyData({'car_body': {'color': 'BLACK', 'type': 'SEDAN', 'components': ['AUTOMATIC TRANSMISSION', 'LED HEADLIGHTS', 'AIR CONDITIONING', 'ALLOY WHEELS','LEATHER SEATS', 'BLUETOOTH']}})
WHEEL_INFO_1 = ValidateWheelData({'wheel': {'type': 'SUMMER', 'model': 'BRIDGESTONE', 'size': 18}})


BASIC_INFO_2 = ValidateBasicData({'model': 'ALFA ROMEO', 'price': 200.0, 'mileage': '2000'})
ENGINE_INFO_2 = ValidateEngineData({'engine': {'type': 'HYBR1D', 'power': 150}})
BODY_INFO_2 = ValidateCarBodyData({'car_body': {'color': 'BLACK', 'type': 'SEDAN', 'components': ['LED HEADLIGHTS', 'led']}})
WHEEL_INFO_2 = ValidateWheelData({'wheel': {'type': 'SUMMER', 'model': 'PIRELLI3', 'size': -18}})

BASIC_INFO_3 = ValidateBasicData({'model': 'BM3W', 'price': '220', 'mileage': -2000})
ENGINE_INFO_3 = ValidateEngineData({'engine': {'type': 1, 'power': -150.0}})
BODY_INFO_3 = ValidateCarBodyData({'car_body': {'color': 'PINK', 'type': 'COUPE', 'components': ['BLUETOOTH', 'BLUETOOTH']}})
WHEEL_INFO_3 = ValidateWheelData({'wheel': {'type': 'ALL-SEASON', 'model': 'pirelli', 'size': 18}})

BASIC_INFO_4 = ValidateBasicData({'model': 'MERCEDES', 'price': -220, 'mileage': 26000})
ENGINE_INFO_4 = ValidateEngineData({'engine': {'type': 'GASOLINE', 'power': '350.0'}})
BODY_INFO_4 = ValidateCarBodyData({'car_body': {'color': 'PINK', 'type': 'COUPE', 'components': []}})
WHEEL_INFO_4 = ValidateWheelData({'wheel': {'type': 'ALL-SEASON', 'model': 'pirelli', 'size': 18}})
