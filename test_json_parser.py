import unittest
from json_parser import check_json_resource


class TestJsonParser(unittest.TestCase):
    def setUp(self):
        self.invalid_path = "invalid_paXth.json"
        self.invalid_json_struct = "test_jsons/invalid_syntax.json"
        self.invalid_AWS_struct = "test_jsons/invalid_AWS_struct.json"
        self.valid_AWS_json = "test_jsons/valid.json"

    def test_file_not_found(self):
        self.assertEqual(
            check_json_resource(self.invalid_path),
            "File not found, try again."
        )

    def test_invalid_argument(self):
        invalid_args = [15, ["list"], True, (1, 3, 4, 6), {"key": "value"}]
        expected_error_msg = "File not found, try again."

        for arg in invalid_args:
            self.assertEqual(
                check_json_resource(arg),
                expected_error_msg
            )

    def test_invalid_json(self):
        self.assertEqual(
            check_json_resource(self.invalid_json_struct),
            "File structure is not valid JSON."
        )

    def test_invalid_policy_document(self):
        self.assertEqual(
            check_json_resource(self.invalid_AWS_struct),
            "File has invalid AWS Policy document structure."
        )

    def test_correct_return(self):
        self.assertIsInstance(
            check_json_resource(self.valid_AWS_json),
            list)
        self.assertEqual(
            check_json_resource(self.valid_AWS_json),
            [False, False, True]
        )


if __name__ == '__main__':
    unittest.main()
