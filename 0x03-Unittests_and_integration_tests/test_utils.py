#!/usr/bin/env python3
"""Defines a test class"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


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
