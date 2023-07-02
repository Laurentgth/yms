from unittest import TestCase
from module_time_offset import format_number_to_2_digits, convert_URL_time_offset_to_mins_and_secs


class TestFormatNumber2Digits(TestCase):

    def test_forbidden_types(self):
        self.assertRaises(TypeError, format_number_to_2_digits, True)
        self.assertRaises(TypeError, format_number_to_2_digits, [1, 2])
        self.assertRaises(TypeError, format_number_to_2_digits, (3, 4))
        self.assertRaises(TypeError, format_number_to_2_digits, {"1234": 5})

    def test_string_is_numeric(self):
        self.assertRaises(TypeError, format_number_to_2_digits, "hello")

    def test_return_values(self):
        self.assertEqual(format_number_to_2_digits('1'), '01')
        self.assertEqual(format_number_to_2_digits(1), '01')
        self.assertEqual(format_number_to_2_digits('01'), '01')
        self.assertEqual(format_number_to_2_digits('13'), '13')
        self.assertEqual(format_number_to_2_digits(13), '13')
        self.assertEqual(format_number_to_2_digits('1234'), '1234')


class TestConvertURLToMinsAndSecs(TestCase):

    def test_return_values_regular_vids(self):
        self.assertEqual(convert_URL_time_offset_to_mins_and_secs(
            "34s"), {"mins": "00", "secs": "34"})
        self.assertEqual(convert_URL_time_offset_to_mins_and_secs(
            "1234"), {"mins": "20", "secs": "34"})
        self.assertEqual(convert_URL_time_offset_to_mins_and_secs(
            "5678s"), {"mins": "94", "secs": "38"})
        self.assertEqual(convert_URL_time_offset_to_mins_and_secs(
            "12m34s"), {"mins": "12", "secs": "34"})
