#!/usr/bin/env python3
'''unittest module'''
import unittest
from unittest.mock import patch, Mock
from utils import get_json
from parameterized import parameterized
from utils import access_nested_map


class TestGetJson(unittest.TestCase):
    '''Json class test'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        '''method to test that utils.get_json
        returns the expected result.'''
        # Patch requests.get to control its behavior
        with patch('utils.requests.get') as mock_get:
            # Configure the mock to return a specific JSON payload
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call get_json with the test URL
            result = get_json(test_url)

            # Assert that requests.get was called once with the correct URL
            mock_get.assert_called_once_with(test_url)

            # Assert that the result matches the expected payload
            self.assertEqual(result, test_payload)


class TestAccessNestedMap(unittest.TestCase):
    '''class that inherits from unittest.TestCase.'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''method to test that the method returns what it is supposed to.'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''This method uses the assertRaises context
        manager to test that a KeyError'''
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        # Verify the exception message matches the missing key
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


if __name__ == '__main__':
    unittest.main()
