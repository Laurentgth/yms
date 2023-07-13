# -*- coding: utf-8 -*-
# ======================================================================
# Created in July 2023
# Author: L. Gauthier @ FizzDevS Designs
# License: MIT
# Description: Youtube Metadata Script (YMS) - A Python script to
#              extract Youtube video metadata
# ======================================================================
# --> Unit tests for prompt module
# ======================================================================
from unittest import TestCase
from module_prompt import process_locator_feed
from module_prompt import standardize_template


class TestProcessLocatorFeed(TestCase):
    def test_return_values_regular_vids(self):
        self.assertEqual(process_locator_feed(
            "l9G7lSS7Buw"), ("l9G7lSS7Buw", None, False))
        self.assertEqual(process_locator_feed(
            "https://youtu.be/l9G7lSS7Buw"), ("l9G7lSS7Buw", None, False))
        self.assertEqual(process_locator_feed(
            "https://www.youtube.com/watch?v=l9G7lSS7Buw&pp=ygUPc3RlZmFuIG1pc2Nob29r"), ("l9G7lSS7Buw", None, False))

    def test_return_values_regular_vids_with_timestamp(self):
        self.assertEqual(process_locator_feed(
            "https://youtu.be/8z_Bx298G0g?t=447"), ("8z_Bx298G0g", "447", False))
        self.assertEqual(process_locator_feed(
            "https://youtu.be/8z_Bx298G0g?t=447s"), ("8z_Bx298G0g", "447s", False))
        self.assertEqual(process_locator_feed(
            "https://youtu.be/8z_Bx298G0g?t=7m27s"), ("8z_Bx298G0g", "7m27s", False))
        self.assertEqual(process_locator_feed(
            "https://www.youtube.com/watch?v=l9G7lSS7Buw&t=3s&pp=ygUPc3RlZmFuIG1pc2Nob29r"), ("l9G7lSS7Buw", "3s", False))
        self.assertEqual(process_locator_feed(
            "https://www.youtube.com/watch?v=l9G7lSS7Buw&t=5s"), ("l9G7lSS7Buw", "5s", False))

    def test_return_values_shorts_vids(self):
        self.assertEqual(process_locator_feed(
            "https://www.youtube.com/shorts/0RhGW1b4hKM"), ("0RhGW1b4hKM", None, False))
        self.assertEqual(process_locator_feed(
            "https://www.youtube.com/shorts/-B5ELVyy_AQ"), ("-B5ELVyy_AQ", None, False))
        self.assertEqual(process_locator_feed(
            "https://youtube.com/shorts/hbLFj0Bw5ug"), ("hbLFj0Bw5ug", None, False))
        self.assertEqual(process_locator_feed(
            "https://youtube.com/shorts/hbLFj0Bw5ug?feature=share"), ("hbLFj0Bw5ug", None, False))
        self.assertEqual(process_locator_feed(
            "https://www.youtube.com/live/dIqcel-B3nA?feature=share"), ("dIqcel-B3nA", None, False))

    def test_prompt_template_request(self):
        self.assertEqual(process_locator_feed(
            "l9G7lSS7Buw -t"), ("l9G7lSS7Buw", None, True))
        self.assertEqual(process_locator_feed(
            "https://youtu.be/l9G7lSS7Buw -t"), ("l9G7lSS7Buw", None, True))
        self.assertEqual(process_locator_feed(
            "https://youtu.be/8z_Bx298G0g?t=447 -t"), ("8z_Bx298G0g", "447", True))
        self.assertEqual(process_locator_feed(
            "https://www.youtube.com/watch?v=l9G7lSS7Buw&t=3s&pp=ygUPc3RlZmFuIG1pc2Nob29r -t"), ("l9G7lSS7Buw", "3s", True))
        self.assertEqual(process_locator_feed(
            "https://www.youtube.com/shorts/0RhGW1b4hKM -t"), ("0RhGW1b4hKM", None, True))
        self.assertEqual(process_locator_feed(
            "https://www.youtube.com/live/dIqcel-B3nA?feature=share   -t"), ("dIqcel-B3nA", None, True))

        self.assertEqual(process_locator_feed(
            "l9G7lSS7Buw --template"), ("l9G7lSS7Buw", None, True))
        self.assertEqual(process_locator_feed(
            "https://youtu.be/l9G7lSS7Buw --template"), ("l9G7lSS7Buw", None, True))
        self.assertEqual(process_locator_feed(
            "https://youtu.be/8z_Bx298G0g?t=447 --template"), ("8z_Bx298G0g", "447", True))
        self.assertEqual(process_locator_feed(
            "https://www.youtube.com/watch?v=l9G7lSS7Buw&t=3s&pp=ygUPc3RlZmFuIG1pc2Nob29r --template"), ("l9G7lSS7Buw", "3s", True))
        self.assertEqual(process_locator_feed(
            "https://www.youtube.com/shorts/0RhGW1b4hKM --template"), ("0RhGW1b4hKM", None, True))
        self.assertEqual(process_locator_feed(
            "https://www.youtube.com/live/dIqcel-B3nA?feature=share   --template"), ("dIqcel-B3nA", None, True))

    def test_for_extra_spaces(self):
        self.assertEqual(process_locator_feed(
            "https://youtu.be/l9G7lSS7Buw "), ("l9G7lSS7Buw", None, False))
        self.assertEqual(process_locator_feed(
            " https://youtu.be/8z_Bx298G0g?t=447"), ("8z_Bx298G0g", "447", False))
        self.assertEqual(process_locator_feed(
            " https://www.youtube.com/watch?v=l9G7lSS7Buw&t=3s&pp=ygUPc3RlZmFuIG1pc2Nob29r "), ("l9G7lSS7Buw", "3s", False))
        self.assertEqual(process_locator_feed(
            " https://www.youtube.com/shorts/0RhGW1b4hKM -t "), ("0RhGW1b4hKM", None, True))
        self.assertEqual(process_locator_feed(
            "https://www.youtube.com/shorts/0RhGW1b4hKM -t "), ("0RhGW1b4hKM", None, True))
        self.assertEqual(process_locator_feed(
            " https://www.youtube.com/live/dIqcel-B3nA?feature=share --template"), ("dIqcel-B3nA", None, True))


class TestStandardizeTemplate(TestCase):
    def test_return_values(self):
        self.assertEqual(standardize_template(
            "Nothing happens here"), "Nothing happens here")
        self.assertEqual(standardize_template(
            "this template prints {vid.id}"), "this template prints {vid_id}")
        self.assertEqual(standardize_template(
            "this one is tricky {{{vid.id}}}!"), "this one is tricky {{{vid_id}}}!")
