"""
-------------------------------------------------------
Tests various array-based sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2019-04-27"
-------------------------------------------------------
"""
# Imports
import random
from random import randint
from Number import Number
from Sorts_array import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
	from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    values = []
    for i in range(SIZE):
        temp_num = Number(i)
        values.append(temp_num)

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
	from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    values = []
    for i in range(SIZE - 1, -1, -1):
        temp_num = Number(i)
        values.append(temp_num)

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """

    arrays = []
    for i in range(SIZE):
        temp = []
        for j in range(TESTS):
            temp.append(Number(randint(0, XRANGE)))
            
        arrays.append(temp)
    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    Number.comparisons=0
    Sorts.swaps=0
    sorted = create_sorted()
    reversed = create_reversed()
    rand = create_randoms()
    
    func(sorted)
    comps1 = round(Number.comparisons)
    swaps1 = round(Sorts.swaps, 0)
    Number.comparisons = 0
    Sorts.swaps = 0
    
    func(reversed)
    comps2 = round(Number.comparisons)
    swaps2 = round(Sorts.swaps, 0)
    Number.comparisons = 0
    Sorts.swaps = 0
    
    for i in rand:        
        func(i)
    comps3 = round(Number.comparisons)
    swaps3 = round(Sorts.swaps, 0)
    Number.comparisons = 0
    Sorts.swaps = 0
    
    print("{:14} {:8} {:8} {:8} {:8} {:8} {:8}".format(title, comps1, comps2, comps3, swaps1, swaps2, swaps3))

    return

print("n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")

for sort in SORTS:
    test_sort(sort[0], sort[1])
