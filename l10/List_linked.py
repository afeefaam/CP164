"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author: Aliyya Wasiq
ID:     169023106
Email:  wasi3106@mylaurier.ca
__updated__ = "2023-12-10"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import deepcopy


class List:
    """
    A linked List class.
    """

    def pair_count(self):
        """
        -------------------------------------------------------
        Returns the number of pairs of values (values that are adjacent
        to each other) in source.
        Use: source.pair_count(n)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            pairs - the number of pairs in source (int >= 0)
        -------------------------------------------------------
        """

        # Your code here

        return

    def rotate_front(self):
        """
        -------------------------------------------------------
        Moves the front node to the rear of the List.
        Use: source.rotate_front()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            None
        -------------------------------------------------------
        """

        # Your code here

        return

    def rotate_rear(self):
        """
        -------------------------------------------------------
        Moves the rear node to the front of the List.
        Use: source.rotate_rear()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            None
        -------------------------------------------------------
        """

        # Your code here

        return

    def has_loop(self):
        """
        -------------------------------------------------------
        Determines if source contains a circular reference/loop.
        Use: loop = source.has_loop()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            loop - True if source contains a circular reference,
                False otherwise (bool)
        -------------------------------------------------------
        """

        # Your code here

        return

    def remove_loop(self):
        """
        -------------------------------------------------------
        Locates and removes any loop in the list. The rear node is preserved.
        Use: source.remove_loop()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            None
        -------------------------------------------------------
        """

        # Your code here

        return


# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        count = 0
        current = self._front

        while current is not None and count < self._count:
            yield current._value
            current = current._next
            count += 1


class _List_Node:
    """
    A linked List Node class.
    """

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
