"""
------------------------------------------------------------------------
[This program reverses the source stack]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-27"
------------------------------------------------------------------------
"""
from Stack_array import Stack 

source=Stack()
source._values=[10,20,30]

print("Original Stack: ", source._values)
source.reverse()
print("Reversed stack: ", source._values)
