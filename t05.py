"""
------------------------------------------------------------------------
[This program splits a priority queue]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-02-03"
------------------------------------------------------------------------
"""
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue
source=Priority_Queue()


source.insert("a")
source.insert("b")
source.insert("c")
source.insert("d")
source.insert("e")
source.insert("f")
key="e"
print("----------")
print(f'Queue:')
print("----------")
for value in source:
    print(value)
target1, target2 = pq_split_key(source, key)
print("----------")
print(f'Target 1:')
print("----------")
for value in target1:
    print(value)
print("----------")
print(f'Target 2:')
print("----------") 
for value in target2:
    print(value)
    
empty=source.is_empty()
print()
print(f'Is it empty?: {empty}')

