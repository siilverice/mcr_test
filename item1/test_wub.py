import unittest

from item1.string_decoder import string_decoder


class TestStringDecoder(unittest.TestCase):
    expected_result = "A B C"

    def test_WUB_should_be_replaced_by_1_space(self):
        self.assertEqual(string_decoder("AWUBBWUBC"), self.expected_result)

    def test_multiples_WUB_should_be_replaced_by_only_1_space(self):
        self.assertEqual(string_decoder("AWUBWUBWUBBWUBWUBWUBC"), self.expected_result)

    def test_heading_or_trailing_spaces_should_be_removed(self):
        self.assertEqual(string_decoder("WUBAWUBBWUBCWUB"), self.expected_result)


if __name__ == '__main__':
    unittest.main()
