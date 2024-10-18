#!/usr/bin/env python3
'''This module contains a function that sum the items
in a list and return the result as a float'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats."""
    return sum(input_list)
