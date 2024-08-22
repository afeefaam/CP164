"""
------------------------------------------------------------------------
[This program splits the source into two targets]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-02-03"
------------------------------------------------------------------------
"""
from Queue_array import Queue
source=Queue()

for i in range(6):
    source.insert(i)
print("----------")
print(f'Source:')
print("----------")
for value in source:
    print(value)
target1, target2 = source.split_alt()
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

