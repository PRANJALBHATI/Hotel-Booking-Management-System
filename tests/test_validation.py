import unittest
from unittest.mock import patch

from src.validation import (
    get_non_empty_input,
    get_positive_number,
    get_positive_integer
)


class TestValidation(unittest.TestCase):

    @patch("builtins.input", side_effect=["Rahul"])
    def test_non_empty_input(self, mock_input):
        result = get_non_empty_input("Enter name: ")
        self.assertEqual(result, "Rahul")

    @patch("builtins.input", side_effect=["1500"])
    def test_positive_number(self, mock_input):
        result = get_positive_number("Enter price: ")
        self.assertEqual(result, 1500.0)

    @patch("builtins.input", side_effect=["2"])
    def test_positive_integer(self, mock_input):
        result = get_positive_integer("Enter nights: ")
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()