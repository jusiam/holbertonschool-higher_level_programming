#!/usr/bin/python3
"""
A CountedIterator class that wraps an iterator
and keeps track of the number of items yielded.
"""


class CountedIterator():
    """
    An iterator that wraps another iterator and
    keeps track of the number of items yielded.

    Args:
        iterator: The underlying iterator
        to be wrapped.count (int, optional):
        he initial count. Defaults to 0.

    Yields:
        The next item from the underlying iterator.

    Raises:
        StopIteration: If there are no more items
        in the underlying iterator.
    """

    def __init__(self, iterator, count=0):
        """
        Initializes the CountedIterator object.

        Args:
            iterator: The underlying iterator
            to be wrapped.
            count (int, optional): The initial
            count. Defaults to 0.
        """
        self.count = count
        self.iter = iter(iterator)

    def get_count(self):
        """
        Returns the current count of items yielded.

        Returns:
            int: The number of items yielded so far.
        """
        return self.count

    def __next__(self):
        """
        Gets the next item from the underlying iterator
        and increments the count.

        Returns:
            The next item from the underlying iterator.

        Raises:
            StopIteration: If there are no more items
            in the underlying iterator.
        """
        try:
            item = next(self.iter)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
