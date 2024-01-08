#!/usr/bin/env python3
"""Defines a test class"""
import unittest
from typing import *
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map function"""

    @parameterized.expand([
        ('one_layer', {'a': 1}, ('a',), 1),
        ('two_layer', {'a': {'b': 2}}, ('a',), {'b': 2}),
        ('three_layer', {"a": {"b": 2}}, ('a', 'b'), 2)
                           ])
    def test_access_nested_map(self, _, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ('empty_map', {}, ('a',), KeyError),
        ('missing_key', {'a': 1}, ('a', 'b'), KeyError),
        ])
    def test_access_nested_map_exception(self, _, nested_map, path, expected):
        with self.assertRaises(expected) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception).strip("'"), path[-1])


class TestGetJson(unittest.TestCase):
    """Test class for get_json method"""

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
        ])
    def test_get_json(self, url, payload):
        """Mock requests.get() """
        mock_response = Mock()
        mock_response.json.return_value = payload
        with patch('requests.get', return_value=mock_response) as mr:
            response = get_json(url)
            self.assertEqual(response, payload)
            mr.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Test memoization"""

    def test_memoize(self):
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_obj = TestClass()
        with patch.object(test_obj, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42

            ans1 = test_obj.a_property
            ans2 = test_obj.a_property
            self.assertEqual(ans1, 42)
            self.assertEqual(ans2, 42)
            mock_a_method.assert_called_once()
