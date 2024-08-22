"""
------------------------------------------------------------------------
[This program tests the array to stack function]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-19"
------------------------------------------------------------------------
"""
from utilities import array_to_stack
from Stack_array import Stack


stack=Stack()
source=[1,2,3,4,5,6,7,8]

array_to_stack(stack, source)

print(f'Source: {source}')

for i in stack:
    print(i)
