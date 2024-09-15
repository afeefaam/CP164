"""
-------------------------------------------------------
Exam: Simple BST testing
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-08-12"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST


# Constants
VALUES = [11, 7, 6, 9, 8, 15, 12, 18]
SEP = '-' * 60


def to_BST(values):
    """
    Testing helper method. Copies Python list values to a BST.
    """
    bst = BST()

    for v in values:
        bst.insert(v)
    return bst


def test_are_siblings():
    """
    Tests the 'are_siblings' method.
    """
    print(SEP)
    print("Test 'are_siblings'")
    print()
    bst = to_BST(VALUES)

    print(f"  Preorder: {bst.preorder()}")
    print(f"  are_siblings(11, 15): {bst.are_siblings(11, 15)}")
    print(f"  are_siblings(7, 15): {bst.are_siblings(7, 15)}")
    print(f"  are_siblings(7, 18): {bst.are_siblings(7, 18)}")


def test_longest_path():
    """
    Tests the 'longest_path' method.
    """
    print(SEP)
    print("Test 'longest_path'")
    print()
    bst = to_BST([])

    print(f"  Preorder: {bst.preorder()}")
    print(f"  Max Path: {bst.longest_path()}")
    print()

    bst = to_BST([VALUES[0]])
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Max Path: {bst.longest_path()}")
    print()

    bst = to_BST(VALUES)
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Max Path: {bst.longest_path()}")


def test_furthest():
    """
    Tests the 'furthest' method.
    """
    print(SEP)
    print("Test 'furthest'")
    print()
    bst = to_BST([])

    print(f"  Preorder: {bst.preorder()}")
    print(f"  Furthest: {bst.furthest()}")
    print()

    bst = to_BST([VALUES[0]])
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Furthest: {bst.furthest()}")
    print()

    bst = to_BST(VALUES)
    print(f"  Preorder: {bst.preorder()}")
    print(f"  Furthest: {bst.furthest()}")


if __name__ == "__main__":
    print("BST_linked Testing")
    test_are_siblings()
    test_longest_path()
    test_furthest()
