#!/usr/bin/env python3
'''This module contains a function to_kv that takes a
string k and an int OR float v as arguments and
returns a tuple.'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string k and the square of v."""
    return (k, float(v ** 2))
