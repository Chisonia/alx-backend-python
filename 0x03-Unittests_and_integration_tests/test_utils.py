#!/usr/bin/env python3
'''unittest module'''
import unittest
from unittest.mock import patch, Mock
from utils import get_json, memoize
from parameterized import parameterized
from utils import access_nested_map


class TestMemoize(unittest.TestCase):

    '''Test case for the `memoize` decorator in the `utils` module.

    This class tests that the `memoize` decorator
    caches the result of a method after the first call,
    ensuring that subsequent calls to the same method
    do not cause it to be executed again,
    but instead return the cached result.'''

    def test_memoize(self):
        '''Test the memoization behavior of the `memoize` decorator.

        This test defines a `TestClass` with a regular method
        `a_method` and a memoized property `a_property`.
        It verifies that:
        1. Calling `a_property` for the first time invokes
        `a_method` and returns its result.
        2. Subsequent calls to `a_property` do not invoke
        `a_method` again but return the cached result.

        Assertions:
            - The first and second calls to `a_property`
            return the same expected value.
            - `a_method` is only called once, verifying that
            the result is cached after the first call.'''
        class TestClass:
            '''A test class with a regular method `a_method`
            and a memoized property `a_property`.
            The `a_property` method uses the `@memoize`
            decorator to cache the result of `a_method`
            after the first call.'''
            def a_method(self):
                '''A simple method that returns
                a static value.'''
                return 42

            @memoize
            def a_property(self):
                '''
                The `@memoize` decorator ensures that
                `a_method` is only called once and that
                subsequent calls to `a_property` return
                the cached result.'''
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test_instance = TestClass()

            # First call to a_property should call a_method
            result_first_call = test_instance.a_property
            self.assertEqual(result_first_call, 42)

            # Second call to a_property should use the memoized
            result_second_call = test_instance.a_property
            self.assertEqual(result_second_call, 42)

            # Ensure a_method was only called once
            mock_method.assert_called_once()


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
