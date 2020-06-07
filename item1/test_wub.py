import unittest

from item1.wub import string_decoder


class MyTestCase(unittest.TestCase):
    def test_WUB_should_be_replaced_by_1_space(self):
        expected_result = "A B C"
        self.assertEqual(expected_result, string_decoder("AWUBBWUBC"))

    def test_multiples_WUB_should_be_replaced_by_only_1_space(self):
        expected_result = "A B C"
        self.assertEqual(expected_result, string_decoder("AWUBWUBWUBBWUBWUBWUBC"))

    def test_heading_or_trailing_spaces_should_be_removed(self):
        expected_result = "A B C"
        self.assertEqual(expected_result, string_decoder("WUBAWUBBWUBCWUB"))


if __name__ == '__main__':
    unittest.main()
