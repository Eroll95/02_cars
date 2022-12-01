import unittest
from app.model import matches_regex
from app.validator.validator import validate_basic_info, validate_engine
from app.model.car import *


class TestValidator(unittest.TestCase):

    def setUp(self) -> None:
        self.car_1 = Car('BMW', Decimal(100), 2000,
                         engine=Engine(EngineType(1), 200),
                         car_body=CarBody(CarBodyColor(1), CarBodyType(2),
                         components=['LED HEADLIGHTS']),
                         wheel=Wheel(TyreType(1), 'PIRELLI', 17))

        self.regex_1 = r'^[A-Z]+$'

    def test_basic_validator_regex(self):
        self.assertTrue(matches_regex(self.regex_1, self.car_1.model))
        self.assertTrue(matches_regex(self.regex_1, 'AUDI'))
        self.assertFalse(matches_regex(self.regex_1, 'AUDIi'))
        self.assertFalse(matches_regex(self.regex_1, 'AUDI3'))
        self.assertFalse(matches_regex(self.regex_1, 'AUD-I'))
        self.assertRegex('AUDI', self.regex_1)

    @unittest.expectedFailure
    def test_regex(self):
        self.assertRegex('audi', self.regex_1)

    def test_validate_basic_info(self):
        self.assertTrue(validate_basic_info(self.car_1))

    @unittest.skip('Problems with engine type and Enums')
    def test_validate_engine(self):
        self.assertTrue(validate_engine(self.car_1.engine))


if __name__ == '__main__':
    unittest.main()
