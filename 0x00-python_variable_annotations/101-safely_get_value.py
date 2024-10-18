#!/usr/bin/env python3
'''This module contains a function
that gets value from a dictionary
or return default if the key is not found.'''
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, T], key: Any, default: Union[T, None] = None
        ) -> Union[T, None]:
    """Safely get a value from a dictionary,
    returning default if the key is not found."""
    if key in dct:
        return dct[key]
    else:
        return default
