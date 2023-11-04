#!/usr/bin/env python3
"""
Module for a type-annotated function floor which
takes a float n as argument and returns the floor of the float.
"""


def floor(a: float) -> int:
    """Type-annotated function which takes a float n as argument and returns
    the floor of the float.

    Args:
        a (float): float to floor.

    Returns:
        int: The floor of the float.
    """
    return int(a)
