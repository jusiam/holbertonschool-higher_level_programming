#!/usr/bin/python3
"""
class VerboseList
"""


class VerboseList(list):
    """class verboselist
    """
    def append(self, item):
        """
        Appends an element to the list and prints a message.

        Args:
            item: The element to be appended.
        """
        super().append(item )
        print(f"Added [{item}] to the list")

    def extend(self, iterable):
        """
        Extends the list with elements from an iterable and prints a message.

        Args:
            iterable: An iterable containing the elements to be added.
        """
        num_added = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{num_added}] items.")

    def remove(self, item):
        """
        Removes the first item from the list with the specified
        item and prints a message.

        Args:
            item: The item of the element to be removed.
        """
        if item in self:
            super().remove(item)
            print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        removed_element = super().pop(index)
        print(f"Popped [{removed_element}] from the list.")
        return removed_element
