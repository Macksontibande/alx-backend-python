#!/usr/bin/env python3
"""
A module for a type-annotated function to_kv that takes a string k and an
int OR float v as arguments and returns a tuple. The first element of the tuple
is the string k. The second element is the square of the int/float v and should
be annotated as a float.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Type-annotated function that takes a string k and an int OR float v
    as arguments and returns a tuple.

    Args:
        k (str): The string to include in the tuple.
        v (Union[int, float]): The integer or float to square and
        include in the tuple.

    Returns:
        Tuple[str, float]: The tuple with the string as the first element
        and the squared integer or float as the second element.
    """
    return (k, float(v**2))
