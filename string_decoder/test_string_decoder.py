import unittest

from string_decoder.main import string_decoder


class TestStringDecoder(unittest.TestCase):
    expected_result = "A B C"

    def test_basic(self):
        self.assertEqual("WE ARE THE BACKYARD MY FRIEND", string_decoder("WUBWEWUBAREWUBWUBTHEWUBBACKYARDWUBMYWUBFRIENDWUB"))

    def test_WUB_should_be_replaced_by_1_space(self):
        self.assertEqual(self.expected_result, string_decoder("AWUBBWUBC"))

    def test_multiples_WUB_should_be_replaced_by_only_1_space(self):
        self.assertEqual(self.expected_result, string_decoder("AWUBWUBWUBBWUBWUBWUBC"))

    def test_heading_or_trailing_spaces_should_be_removed(self):
        self.assertEqual(self.expected_result, string_decoder("WUBAWUBBWUBCWUB"))


if __name__ == '__main__':
    unittest.main()
