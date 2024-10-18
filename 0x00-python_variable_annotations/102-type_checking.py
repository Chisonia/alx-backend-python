#!/usr/bin/env python3
'''This module contains a function that zooms in
on array by repeating each element number of times'''
from typing import List, Tuple


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """Zooms in on the array by repeating each
    element `factor` times."""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
