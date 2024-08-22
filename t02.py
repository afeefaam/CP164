"""
------------------------------------------------------------------------
[This program tests task 2]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-27"
------------------------------------------------------------------------
"""
from Stack_array import Stack

stack1=Stack()
stack2=Stack()

stack1._values=[8,12,8,5]
stack2._values=[14, 9, 7, 1, 6, 3]

target=Stack()

target.combine(stack1, stack2)

