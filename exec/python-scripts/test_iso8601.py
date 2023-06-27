from unittest import TestCase
from iso8601 import convert_2_digits, parse_iso_duration


class TestConvert2Digits(TestCase):
    def test_forbidden_types(self):
        self.assertRaises(TypeError, convert_2_digits, True)
        self.assertRaises(TypeError, convert_2_digits, [1, 2])

    def test_string_is_numeric(self):
        self.assertRaises(TypeError, convert_2_digits, "hello"
                          )

    def test_return_values(self):
        self.assertEqual(convert_2_digits('1'), '01')
        self.assertEqual(convert_2_digits(1), '01')
        self.assertEqual(convert_2_digits('01'), '01')
        self.assertEqual(convert_2_digits('13'), '13')
        self.assertEqual(convert_2_digits(13), '13')
        self.assertEqual(convert_2_digits('1234'), '1234')


class TestParseIsoDuration(TestCase):
    def test_return_values(self):
        self.assertEqual(parse_iso_duration("PT3M2S"), ("03", "02"))
        self.assertEqual(parse_iso_duration("PT3M22S"), ("03", "22"))
        self.assertEqual(parse_iso_duration("PT15M22S"), ("15", "22"))
        self.assertEqual(parse_iso_duration("PT21M1S"), ("21", "01"))
        self.assertEqual(parse_iso_duration("PT1H17M15S"), ("77", "15"))
