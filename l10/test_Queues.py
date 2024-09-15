"""
-------------------------------------------------------
Exam: Simple Queues testing
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-12-10"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from Queue_linked import Queue
from Priority_Queue_linked import _PQ_Node, Priority_Queue

# Constants
VALUES = [3, 8, 6, 7, 6, 2, 4, 6]
SEP = '-' * 60


def to_python_list(source):
    """
    Testing helper method. Copies Queue values to a Python list.
    """
    values = []
    for value in source:
        values.append(value)
    return values


def to_Queue(values):
    """
    Testing helper method. Copies Python list values to a Queue.
    """
    source = Queue()
    for value in values:
        source.insert(value)
    return source


def to_Priority_Queue(values):
    """
    Testing helper method. Copies Python list values to a Priority_Queue.
    """
    source = Priority_Queue()
    for value in values:
        source.insert(value)
    return source


def test_move_node():
    """
    Tests the '_move_node' method.
    """
    print(SEP)
    print("Test '_move_node'")
    print()

    source = to_Priority_Queue(VALUES)
    print(f"    Priority_Queue': {to_python_list(source)}")
    node = _PQ_Node(0, None)
    print(f"    node: 0")
    source._move_node(node)
    print(f"    Priority_Queue': {to_python_list(source)}")
    node = _PQ_Node(99, None)
    print(f"    node: 99")
    source._move_node(node)
    print(f"    Priority_Queue': {to_python_list(source)}")
    node = _PQ_Node(5, None)
    print(f"    node: 5")
    source._move_node(node)
    print(f"    Priority_Queue': {to_python_list(source)}")


def test_to_priority_queue():
    """
    Tests the 'to_priority_queue' method.
    """
    print(SEP)
    print("Test 'to_priority_queue'")
    print()

    source = to_Queue(VALUES)
    print(f"  Queue: {to_python_list(source)}")
    pq = source.to_priority_queue()
    print(f"    Queue: After 'to_priority_queue': {to_python_list(source)}")
    print(f"    Priority_Queue': {to_python_list(pq)}")
    print()


def test_sum_consecutive():
    """
    Tests the 'sum_consecutive' method.
    """
    print(SEP)
    print("Test 'sum_consecutive'")
    print()

    source = to_Queue([3, 3, 7, 4, 4, 4, 5])
    print(f"  Queue: {to_python_list(source)}")
    source.sum_consecutive()
    print(f"    Queue: After 'sum_consecutive': {to_python_list(source)}")
    print()


if __name__ == "__main__":
    print("Queue_linked and Priority_Queue_linked Testing")
    test_move_node()
    test_sum_consecutive()
    test_to_priority_queue()
