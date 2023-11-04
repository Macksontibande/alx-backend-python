#!/usr/bin/env python3
"""
This is a module that provides a function for zooming in on a tuple.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    This function takes a tuple and a zoom factor, and returns a new list
        with the elements of the tuple repeated according to the zoom factor.

    Parameters:
    lst (Tuple): The tuple to zoom in on.
    factor (int): The zoom factor, which determines how many times each
        element of the tuple should be repeated in the output list.

    Returns:
    List: A new list with the elements of the tuple repeated according to
        the zoom factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

# :man: Author and Credits.
This project was done by [SE. Mackson Mthembu](https://github.com/Macksontibande). Feel free to get intouch with me;

:iphone: WhatsApp [+27677892449](https://wa.me/+27677892449)

:email: Email [Macksontibande@gmail.com](mailto:Macksontibade@gmail.com)

:thumbsup: A lot of thanks to [ALX-Africa Software Engineering](https://www.alxafrica.com/) program for the project requirements.
