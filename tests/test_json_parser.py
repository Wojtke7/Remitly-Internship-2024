import unittest
import json
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from json_parser import json_parser


class TestJsonParser(unittest.TestCase):
    def setUp(self):
        self.invalid_path = "invalidpath123.json"
        self.invalid_json_struct = "tests/data/invalid_syntax.json"
        self.invalid_AWS_struct = "tests/data/invalid_aws_struct.json"
        self.valid_AWS_json = "tests/data/valid.json"

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            json_parser(self.invalid_path)

    def test_invalid_argument(self):
        invalid_args = [15, ["list"], True, (1, 3, 4, 6), {"key": "value"}]

        for arg in invalid_args:
            with self.assertRaises(Exception):
                json_parser(arg)

    def test_invalid_json(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            json_parser(self.invalid_json_struct)

    def test_invalid_policy_document(self):
        with self.assertRaises(KeyError):
            json_parser(self.invalid_AWS_struct)

    def test_correct_return(self):
        result = json_parser(self.valid_AWS_json)
        self.assertIsInstance(result, list)
        self.assertEqual(result, [False, False, True])

if __name__ == '__main__':
    unittest.main()
