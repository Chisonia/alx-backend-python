#!/usr/bin/env python3
'''This module contains function that returns
elements of a list of nothing if the list is empty'''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of the list
    or None if the list is empty."""
    if lst:
        return lst[0]
    else:
        return None
