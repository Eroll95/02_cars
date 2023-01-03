# from app.validator.validator import validate_name, validate_price, validate_mileage


# -----------LEGACY CODE


# class ValidatorValidateBasicData(unittest.TestCase):
#     def test_object_has_correct_name(self):
#         self.assertTrue(validate_name(CAR_1))
#
#     def test_object_has_incorrect_name_contains_whitespaces(self):
#         self.assertFalse(validate_name(CAR_2))
#
#     def test_object_has_incorrect_name_contains_numbers(self):
#         self.assertFalse(validate_name(CAR_3))
#
#     # TEST Mileage -----------------------------------------------------
#
#     def test_object_has_correct_mileage(self):
#         self.assertTrue(validate_mileage(CAR_1))
#
#     def test_object_has_incorrect_mileage_contains_string(self):
#         self.assertFalse(validate_mileage(CAR_2))
#
#     def test_object_has_incorrect_mileage_contains_negative_value(self):
#         self.assertFalse(validate_mileage(CAR_3))
#
#     # TEST Price -----------------------------------------------------
#
#     def test_object_has_correct_price(self):
#         self.assertTrue(validate_price(CAR_1))
#
#     def test_object_has_incorrect_price_contains_integer(self):
#         self.assertFalse(validate_price(CAR_2))
#
#     def test_object_has_incorrect_price_contains_string(self):
#         self.assertFalse(validate_price(CAR_3))
#
#     def test_object_has_incorrect_price_contains_negative_decimal(self):
#         self.assertFalse(validate_price(CAR_4))
