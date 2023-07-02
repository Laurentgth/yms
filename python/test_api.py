from unittest import TestCase
from module_api import extract_id_and_offset, create_API_URL_to_call, call_API


class TestExtractIDAndOffset(TestCase):

    def test_return_values_regular_vids(self):
        self.assertEqual(extract_id_and_offset(
            "https://youtu.be/l9G7lSS7Buw"), ("l9G7lSS7Buw", None))
        self.assertEqual(extract_id_and_offset(
            "https://www.youtube.com/watch?v=l9G7lSS7Buw&pp=ygUPc3RlZmFuIG1pc2Nob29r"), ("l9G7lSS7Buw", None))

    def test_return_values_regular_vids_with_time_offset(self):
        self.assertEqual(extract_id_and_offset(
            "https://youtu.be/8z_Bx298G0g?t=447"), ("8z_Bx298G0g", "447"))
        self.assertEqual(extract_id_and_offset(
            "https://youtu.be/8z_Bx298G0g?t=447s"), ("8z_Bx298G0g", "447s"))
        self.assertEqual(extract_id_and_offset(
            "https://youtu.be/8z_Bx298G0g?t=7m27s"), ("8z_Bx298G0g", "7m27s"))
        self.assertEqual(extract_id_and_offset(
            "https://www.youtube.com/watch?v=l9G7lSS7Buw&t=3s&pp=ygUPc3RlZmFuIG1pc2Nob29r"), ("l9G7lSS7Buw", "3s"))
        self.assertEqual(extract_id_and_offset(
            "https://www.youtube.com/watch?v=l9G7lSS7Buw&t=5s"), ("l9G7lSS7Buw", "5s"))

    def test_return_values_shorts_vids(self):
        self.assertEqual(extract_id_and_offset(
            "https://www.youtube.com/shorts/0RhGW1b4hKM"), ("0RhGW1b4hKM", None))
        self.assertEqual(extract_id_and_offset(
            "https://www.youtube.com/shorts/-B5ELVyy_AQ"), ("-B5ELVyy_AQ", None))
        self.assertEqual(extract_id_and_offset(
            "https://youtube.com/shorts/hbLFj0Bw5ug"), ("hbLFj0Bw5ug", None))
        self.assertEqual(extract_id_and_offset(
            "https://youtube.com/shorts/hbLFj0Bw5ug?feature=share"), ("hbLFj0Bw5ug", None))
        self.assertEqual(extract_id_and_offset(
            "https://www.youtube.com/live/dIqcel-B3nA?feature=share"), ("dIqcel-B3nA", None))


class TestCreateAPIURLToCall(TestCase):

    def test_return_value(self):
        self.assertEqual(create_API_URL_to_call("8z_Bx298G0g", "XXXX"
                                                ), "https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails&key=XXXX&id=8z_Bx298G0g")
