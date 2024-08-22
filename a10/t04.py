"""
------------------------------------------------------------------------
[This program tests the fourth task.]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-03-28"
------------------------------------------------------------------------
"""
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()
a.insert_front(56)
a.insert_front(54)
a.insert_front(133)
a.insert_front(3)
a.insert_front(35)
a.insert_front(52)
a.insert_front(15423120)

Sorts.gnome_sort(a)

print(f'The values using the Gnome sort is as follows.') 
for i in a:
    print(i)
