"""
------------------------------------------------------------------------
[This program combines two source stacks into one stack.]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-27"
------------------------------------------------------------------------
"""
from functions import stack_combine
from Stack_array import Stack

first_list=[8,12,8,5]
source1=Stack()
for i in first_list:
    source1.push(i)
    
second_list=[14,9, 7, 1, 6, 3]
source2=Stack()
for i in second_list:
    source2.push(i)

target=stack_combine(source1, source2)

print("Target:")


while not target.is_empty():
    print(target.pop())