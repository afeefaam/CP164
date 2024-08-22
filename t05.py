"""
------------------------------------------------------------------------
[This program tests the stack using the foods file]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-19"
------------------------------------------------------------------------
"""
from utilities import stack_newtest
from Stack_array import Stack
from Food_utilities import read_foods

file_variable=open("foods.txt", "r")
source=read_foods(file_variable)
stack=Stack()

stack_newtest(stack, source)

for i in stack:
    print(i)

file_variable.close()