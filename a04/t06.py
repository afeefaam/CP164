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
from Priority_Queue_array import Priority_Queue
source=Priority_Queue()


source.insert("t")
source.insert("i")
source.insert("o")
source.insert("p")
source.insert("g")
source.insert("k")
key="g"

print("----------")
print(f'Queue:')
print("----------")

for value in source:
    print(value)
target1, target2 = source.split_key(key)

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
