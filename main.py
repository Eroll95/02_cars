from services.car_service import CarService
from typing import Final
from services.types import SortType


def main() -> None:
    cars_filename: Final = r'resources\cars.json'
    cs = CarService(cars_filename)
    # print(cs)
    # print(cs.get_cars_sorted_by_selected_criteria('components quantity'))
    # print(cs.get_cars_sorted_by_selected_criteria_v2(SortType(1), False))
    # print(cs.get_cars_sorted_by_model_with_selected_engine('GASOLINE'))
    # print(cs.get_cars_sorted_by_model_with_selected_car_body('SEDAN', 150, 400))
    # print(cs.get_cars_statistics('price'))
    # print(cs.get_dict_of_tyre_type())
    # print(cs.get_dict_of_car_mileage())
    # print(cs.get_cars_with_selected_component('SPORT PACKAGE'))
    print(cs.get_first_one())


if __name__ == '__main__':
    main()
