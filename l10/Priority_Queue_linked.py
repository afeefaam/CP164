"""
-------------------------------------------------------
linked version of the Priority Queue ADT.
-------------------------------------------------------
Author: Aliyya Wasiq
ID:     169023106
Email:  wasi3106@mylaurier.ca
__updated__ = "2023-08-16"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import deepcopy


class Priority_Queue:
    """
    A linked Priority Queue class.
    """

    def _move_node(self, node):
        """
        -------------------------------------------------------
        Moves node into source at the correct position.
        Use: source._insert_node(source)
        -------------------------------------------------------
        Parameters:
            source - a linked node (PQ_Node / Stack_Node / Queue_Node / List_Node)
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
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def insert(self, value):
        """
        -------------------------------------------------------
        A copy of value is inserted into the priority queue.
        Values are stored in priority order.
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            None
        -------------------------------------------------------
        """
        if self._front is None:
            # Priority queue is empty
            node = _PQ_Node(value, None)
            self._front = node
            self._rear = node
        elif value < self._front._value:
            # New value has highest priority
            self._front = _PQ_Node(value, self._front)
        elif value >= self._rear._value:
            # New value has lowest priority
            node = _PQ_Node(value, None)
            self._rear._next = node
            self._rear = node
        else:
            # Find the proper position for value.
            prev = None
            curr = self._front

            while value >= curr._value:
                prev = curr
                curr = curr._next

            # Create the new node and link it to curr.
            # The previous node is linked to the new node.
            prev._next = _PQ_Node(value, curr)
        # Increment the priority queue size.
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in pq:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        curr = self._front

        while curr is not None:
            yield curr._value
            curr = curr._next


class _PQ_Node:
    """
    A linked Priority Queue Node class.
    """

    def __init__(self, value, _next):
        """
        -------------------------------------------------------
        Initializes a priority queue node that contains a copy of value
        and a link to the next node in the priority queue
        Use: node = _PQ_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _next - another priority queue node (_PQ_Node)
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            a new Priority_Queue object (_PQ_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = _next
