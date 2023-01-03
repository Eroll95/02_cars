from service.car_service import CarService
from typing import Final
from data_loader.json_loader import get_cars
from app.model.car import TyreType
from app.validator.basic_validator import is_value_of


def main() -> None:
    try:
        cars_filename: Final[str] = r'resources/cars.json'
        cs = CarService(get_cars(cars_filename))

        # print(cs)
        # print(cs.get_cars_sorted_by_selected_criteria(SortType.SIZE, False))
        # print(cs.get_cars_sorted_by_model_with_selected_engine('GASOLINE'))
        # print(cs.get_cars_sorted_by_model_with_selected_car_body('SEDAN', 150, 400))
        # print(cs.get_cars_statistics(StatisticsCriteria.POWER))
        # print(cs.get_dict_of_tyre_type())
        # print(cs.get_dict_of_car_mileage())
        # print(cs.get_cars_with_selected_component('SPORT PACKAGE'))
        # print(cs.get_cars_with_price_between(Decimal(100), Decimal(220)))
        print(cs.get_single_car())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    is_value_of(TyreType, 'test')
    # main()

# TODO uporządkować paczki
