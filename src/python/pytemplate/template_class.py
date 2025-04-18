"""A template file defines a demo class

Created by Chongdan Pan (20241024)
"""

from __future__ import annotations


class TemplateClass(object):
    """A class template"""

    def __init__(self, num: int):
        self._num = num

    def get_data(self, num: int) -> list[int]:
        """Get a list of int

        Args:
            num: The count of the int

        Returns:
            A list of int
        """
        return [self._num] * num
