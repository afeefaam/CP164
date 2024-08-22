"""
------------------------------------------------------------------------
[This program tests the stack to array function]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-19"
------------------------------------------------------------------------
"""

from utilities import stack_to_array
from Stack_array import Stack

target=[3,2,1,0,9,5,6]
stack=Stack()
for item in target:
    stack.push(item)

stack_to_array(stack, target)
print(target)