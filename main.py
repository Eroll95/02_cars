from services import car_service
from typing import Final


def main() -> None:
    cars_filename: Final = r'resources\cars.json'
    cs = car_service.CarService(cars_filename)
    print(cs.print_file())


if __name__ == '__main__':
    main()
