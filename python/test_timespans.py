# -*- coding: utf-8 -*-
# ======================================================================
# Created in July 2023
# Author: L. Gauthier @ FizzDevS Designs
# License: MIT
# Description: Youtube Metadata Script (YMS) - A Python script to
#              extract Youtube video metadata
# ======================================================================
# --> Unit tests for timespans module
# ======================================================================
from unittest import TestCase
from module_timespans import parse_iso8601
from module_timespans import format_duration
from module_timespans import convert_timestamp_URL_to_mins_and_secs


class TestParseIsoDuration(TestCase):
    def test_return_values(self):
        self.assertEqual(parse_iso8601("PT42S"), (0, 0, 0, 42))
        self.assertEqual(parse_iso8601("PT23M"), (0, 0, 23, 0))
        self.assertEqual(parse_iso8601("PT3M2S"), (0, 0, 3, 2))
        self.assertEqual(parse_iso8601("PT4H22S"), (0, 4, 0, 22))
        self.assertEqual(parse_iso8601("PT1H17M15S"), (0, 1, 17, 15))
        self.assertEqual(parse_iso8601("P1DT2H32M17S"), (1, 2, 32, 17))
        self.assertEqual(parse_iso8601("P0D"),
                         ("live", "live", "live", "live"))


class TestFormatDuration(TestCase):
    def test_forbidden_types(self):
        self.assertRaises(TypeError, format_duration, True)
        self.assertRaises(TypeError, format_duration, [1, 2])
        self.assertRaises(TypeError, format_duration, (3, 4))
        self.assertRaises(TypeError, format_duration, {"1234": 5})

    def test_string_is_numeric(self):
        self.assertRaises(TypeError, format_duration, "hello")

    def test_return_values(self):
        self.assertEqual(format_duration('live'), 'live')
        self.assertEqual(format_duration('1'), '01')
        self.assertEqual(format_duration(1), '01')
        self.assertEqual(format_duration('01'), '01')
        self.assertEqual(format_duration('13'), '13')
        self.assertEqual(format_duration(13), '13')
        self.assertEqual(format_duration('1234'), '1234')


class TestConvertTimestampUrlToMinsAndSecs(TestCase):
    def test_return_values_regular_vids(self):
        self.assertEqual(convert_timestamp_URL_to_mins_and_secs(
            "34s"), {"mins": "00", "secs": "34"})
        self.assertEqual(convert_timestamp_URL_to_mins_and_secs(
            "1234"), {"mins": "20", "secs": "34"})
        self.assertEqual(convert_timestamp_URL_to_mins_and_secs(
            "5678s"), {"mins": "94", "secs": "38"})
        self.assertEqual(convert_timestamp_URL_to_mins_and_secs(
            "12m34s"), {"mins": "12", "secs": "34"})
