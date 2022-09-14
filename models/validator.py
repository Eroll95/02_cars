from models.car import Car, CarBody, Wheel, Engine
import logging


logging.basicConfig(level=logging.INFO)


def validate_basic_info(car: 'Car') -> bool:
    def validate_name() -> bool:
        if isinstance(car.model, str) and car.model.isupper() and car.model.isalpha():
            return True
        return False

    def validate_price() -> bool:
        if isinstance(car.price, int) and (0 < car.price < 10000000):
            return True
        return False

    def validate_mileage() -> bool:
        if isinstance(car.mileage, int) and (0 < car.mileage < 1000000):
            return True
        return False

    def validate_engine_type() -> bool:
        if isinstance(car.engine.type, str) and car.engine.type.isupper() and car.engine.type.isalpha():
            return True
        return False

    def validate_engine_power() -> bool:
        if isinstance(car.engine.power, float) and (0 < car.engine.power < 2000):
            return True
        return False

    if validate_name() and validate_price() and validate_mileage() and validate_engine_type() and validate_engine_power():
        return True
    return False


def validate_car_body(car_body: 'CarBody') -> bool:
    def validate_color() -> bool:
        if isinstance(car_body.color, str) and car_body.color.isupper() and car_body.color.isalpha():
            return True
        return False

    def validate_type() -> bool:
        if isinstance(car_body.type, str) and car_body.type.isupper() and car_body.type.isalpha():
            return True
        return False

    def validate_components() -> bool:
        if False in [comp.isupper() for comp in car_body.components]:
            return False
        return True

    if validate_color() and validate_type() and validate_components():
        return True
    return False


def validate_wheel(wheel: 'Wheel') -> bool:
    def validate_type() -> bool:
        if isinstance(wheel.type, str) and wheel.type.isupper() and wheel.type.isalpha():
            return True
        return False

    def validate_model() -> bool:
        if isinstance(wheel.model, str) and wheel.model.isupper() and wheel.model.isalpha():
            return True
        return False

    def validate_size() -> bool:
        if isinstance(wheel.size, int) and (12 < wheel.size < 25):
            return True
        return False

    if validate_type() and validate_model() and validate_size():
        return True
    return False


def validate_car(car: 'Car') -> bool:
    if validate_basic_info(car) and validate_car_body(car.carBody) and validate_wheel(car.wheel):
        return True
    return False
