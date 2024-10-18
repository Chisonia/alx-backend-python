#!/usr/bin/env python3
'''This module contains a function that iterate
through a sequence and return a lists of tuple
containing each element'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing each element and its length."""
    return [(i, len(i)) for i in lst]
