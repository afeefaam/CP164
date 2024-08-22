"""
------------------------------------------------------------------------
[This program reverses the content of the stack]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-27"
------------------------------------------------------------------------
"""
from Stack_array import Stack
from functions import stack_reverse

source=Stack()
elements=[10,20,30,40,50]
for index in elements:
    source.push(index)
    
print("Original Stack: ")
for value in source:
    print(value)
    
stack_reverse(source)

print("Reversed Stack: ")
for i in source:
    print(i)
