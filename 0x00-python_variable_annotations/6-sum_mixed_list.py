#!/usr/bin/env python3
'''The module takes a list of different types (int and float)
as an argument and returns their sum as float'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of integers and floats."""
    return float(sum(mxd_lst))

