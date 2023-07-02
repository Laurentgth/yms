from unittest import TestCase
from module_iso8601 import parse_iso_duration


class TestParseIsoDuration(TestCase):
    def test_return_values(self):
        self.assertEqual(parse_iso_duration("PT3M2S"), ("03", "02"))
        self.assertEqual(parse_iso_duration("PT3M22S"), ("03", "22"))
        self.assertEqual(parse_iso_duration("PT15M22S"), ("15", "22"))
        self.assertEqual(parse_iso_duration("PT21M1S"), ("21", "01"))
        self.assertEqual(parse_iso_duration("PT1H17M15S"), ("77", "15"))
