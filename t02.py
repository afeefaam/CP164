"""
------------------------------------------------------------------------
[This program tests the second task.]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-03-28"
------------------------------------------------------------------------
"""
from Sorts_List_linked import Sorts
from List_linked import List

a = List()
a.append(55)
a.append(50)
a.append(983)
a.append(3)
a.append(87)
a.append(45)
a.append(345678)

Sorts.radix_sort(a)
print(f'The smallest value is {a._front._value}.')
