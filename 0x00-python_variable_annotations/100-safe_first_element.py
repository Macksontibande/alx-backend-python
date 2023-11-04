#!/usr/bin/env python3
"""
Module for task 10.
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    This function returns the first element of a sequence, or None if the
        sequence is empty.

    Parameters:
    lst (Sequence): The sequence to process.

    Returns:
    Union[object, None]: The first element of the sequence, or None if the
        sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
