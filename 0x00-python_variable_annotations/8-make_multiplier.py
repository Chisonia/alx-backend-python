#!/usr/bin/env python3
'''This module contains a function make_multiplier
that takes a float multiplier as argument and
returns a function that multiplies a float by multiplier.'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by
    the given multiplier."""

    def multiply(value: float) -> float:
        return multiplier * value

    return multiply
