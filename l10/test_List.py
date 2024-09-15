"""
-------------------------------------------------------
Exam: Simple List testing
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-12-10"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from List_linked import List

# Constants
VALUES = [3, 8, 6, 7, 7, 6, 2, 2, 2, 4, 12]
SEP = '-' * 60


def to_python_list(source):
    """
    Testing helper method. Copies List values to a Python list.
    """
    values = []
    for value in source:
        values.append(value)
    return values


def to_List(values):
    """
    Testing helper method. Copies Python list values to a List.
    """
    source = List()
    for value in values:
        source.append(value)
    return source


def test_pair_count():
    """
    Tests the 'pair_count' method.
    """
    print(SEP)
    print("Test 'pair_count'")
    print()

    source = to_List(VALUES)
    print(f"  List: {to_python_list(source)}")
    pairs = source.pair_count()
    print(f"  pairs: {pairs}")
    print()


def test_rotate_front():
    """
    Tests the 'rotate_front' method.
    """
    print(SEP)
    print("Test 'rotate_front'")
    print()

    source = List()
    print(f"  List: {to_python_list(source)}")
    source.rotate_front()
    print(f"  After 'rotate_front': {to_python_list(source)}")
    print()

    source = to_List(VALUES[:1])
    print(f"  List: {to_python_list(source)}")
    source.rotate_front()
    print(f"  After 'rotate_front': {to_python_list(source)}")
    print()

    source = to_List(VALUES)
    print(f"  List: {to_python_list(source)}")
    source.rotate_front()
    print(f"  After 'rotate_front': {to_python_list(source)}")
    print()


def test_rotate_rear():
    """
    Tests the 'rotate_rear' method.
    """
    print(SEP)
    print("Test 'rotate_rear'")
    print()

    source = List()
    print(f"  List: {to_python_list(source)}")
    source.rotate_rear()
    print(f"  After 'rotate_rear': {to_python_list(source)}")
    print()

    source = to_List(VALUES[:1])
    print(f"  List: {to_python_list(source)}")
    source.rotate_rear()
    print(f"  After 'rotate_rear': {to_python_list(source)}")
    print()

    source = to_List(VALUES)
    print(f"  List: {to_python_list(source)}")
    source.rotate_rear()
    print(f"  After 'rotate_rear': {to_python_list(source)}")
    print()


def test_has_loop():
    """
    Tests the 'has_loop' method.
    """
    print(SEP)
    print("Test 'has_loop'")
    print()

    source = List()
    print(f"  List: {to_python_list(source)}")
    print(f"  Has Loop: {source.has_loop()}")
    print()

    source = to_List(VALUES)
    print(f"  List: {to_python_list(source)}")
    print(f"  Has Loop: {source.has_loop()}")
    print()

    print("  source._rear._next = source._rear")
    source._rear._next = source._rear
    print(f"  Has Loop: {source.has_loop()}")
    print()

    print("  source._front._next._next._next = source._front._next")
    source._front._next._next._next = source._front._next
    print(f"  Has Loop: {source.has_loop()}")
    print()

    print("  source._front._next = source._front")
    source._front._next = source._front
    print(f"  Has Loop: {source.has_loop()}")
    print()


def test_remove_loop():
    """
    Tests the 'remove_loop' method.
    """
    print(SEP)
    print("Test 'remove_loop'")
    print()
    source = to_List(VALUES)
    print("Original list")
    print(f"  List: {to_python_list(source)}")
    print("  source._front._next._next._next = source._front._next")
    source._front._next._next._next = source._front._next
    print(f"  List: {to_python_list(source)}")
    source.remove_loop()
    print("Loop removed")
    print(f"  List: {to_python_list(source)}")
    print()


if __name__ == "__main__":
    print("List_linked Testing")
    # test_pair_count()
    # test_rotate_front()
    # test_rotate_rear()
    # test_has_loop()
    test_remove_loop()
