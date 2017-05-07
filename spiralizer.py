"""
Spiralizer
- Check for valid input. List should have same number of elements in every row
- Edge cases: 1xN array, empty array, even-number array, odd-number array
"""
import sys


class Spiralizer(object):
    """
    Spiralizer provides a spiral iterator to N-by-M arrays

    The spiral goes from the top-left (0, 0) position, clockwise, to the
    center position

    Usage Example:
    ```
    >>> for element in Spiralizer(array):
    ...     print(element)
    ```
    """
    def __init__(self, array):
        self.array = array
        self.validate_array()  # Raises ValueError

    def validate_array(self):
        """
        Determine whether the array can be spiralized

        Returns `True` if the array can be spiralized
        Raises `ValueError` otherwise
        """
        if len(self.array) == 0:
            # An empty array can technically be spiralized
            return True

        first_len = None

        for subarray in self.array:
            try:
                if first_len is None:
                    first_len = len(subarray)
                elif len(subarray) != first_len:
                    raise ValueError(
                        "The input contains subelements of different lengths")
            except TypeError as err:
                # At least one of the subarrays is bad
                raise ValueError(
                    "The input contains subelements that are not iterable")

        return True

    def __iter__(self):
        """
        To achieve a spiralized iteration, we should repeatedly yield each
        value along the outermost uniterated square until completion
        """
        depth = 0

        while depth < len(self.array) / 2:
            for elem in self._iterate_square(depth):
                yield elem
            depth += 1

    def _iterate_square(self, depth):
        """Iterates over the square at depth `depth` from `array`"""
        # Top side going right.  Yield the corners
        row = self.array[depth]
        for elem in row[depth:len(row)-depth]:
            yield elem

        # Right side going down.  Don't yield the corners
        for row in self.array[depth + 1:len(self.array) - depth - 1]:
            yield row[len(row) - depth - 1]

        # Bottom side going left.  Yield the corners
        if len(self.array) - depth - 1 <= depth:
            raise StopIteration()

        row = self.array[len(self.array) - depth - 1]
        for elem in reversed(row[depth:len(row) - depth]):
            yield elem

        # Left side going up.  Don't yield the corners
        for row in reversed(self.array[depth + 1:len(self.array) - depth - 1]):
            yield row[depth]
