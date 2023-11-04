#!/usr/bin/env python3
"""
A module that takes the code from wait_n and alter it into a new
function task_wait_n. The code is nearly identical to
wait_n except task_wait_random is being called.
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Creates a list of tuples, where each tuple contains a string from
    the given list and its length.

    Args:
        lst (List[str]): The list of strings to process.

    Returns:
         List[Tuple[str, int]]: A list of tuples, where each tuple contains
         a string from the original list and its length.
    """
    return [(i, len(i)) for i in lst]
