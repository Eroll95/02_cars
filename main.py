from services import car_service
from typing import Final


def main() -> None:
    cars_filename: Final = r'resources\test_car.json'
    cs = car_service.CarService(cars_filename)
    print(cs)
    print(cs.print_obj())


if __name__ == '__main__':
    main()
