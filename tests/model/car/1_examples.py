from tests.data import CAR_1
from app.model import CarBodyType, CarBodyColor


def engine_test():
    # print([body for body in CarBodyType])
    car1_body = CAR_1.car_body.type
    example_body = CarBodyType(1)
    car1_has_body = CAR_1.car_body.has_body_type(example_body)
    print(car1_body, example_body, car1_has_body)

    car1_color = CAR_1.car_body.color
    example_color = CarBodyColor(1)
    car1_has_color = CAR_1.car_body.has_color(example_color)
    print(car1_color, example_color, car1_has_color)


if __name__ == '__main__':
    engine_test()
