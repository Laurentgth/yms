# -*- coding: utf-8 -*-
# ======================================================================
# Created in July 2023
# Author: L. Gauthier @ FizzDevS Designs
# License: MIT
# Description: Youtube Metadata Script (YMS) - A Python script to
#              extract Youtube video metadata
# ======================================================================
# --> Unit tests for API module
# ======================================================================
from unittest import TestCase
from module_api import create_API_URL_to_call


class TestCreateAPIURLToCall(TestCase):
    def test_return_value(self):
        target_ID = "8z_Bx298G0g"
        fake_key = "XXXX"
        target_URL = "https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails&key=XXXX&id=8z_Bx298G0g"
        self.assertEqual(create_API_URL_to_call(
            target_ID, fake_key), target_URL)
