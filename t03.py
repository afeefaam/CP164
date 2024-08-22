"""
------------------------------------------------------------------------
[This program splits the sources into two queues]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-02-03"
------------------------------------------------------------------------
"""
from Queue_array import Queue
from functions import queue_split_alt

source=Queue()
source.insert(23)
source.insert(24)
source.insert(3)
source.insert(66)
source.insert(29)
print("----------")
print(f'Source:')
print("----------")
for value in source:
    print(value)
target1, target2 = queue_split_alt(source)
print("----------")
print(f'Target 1:')
print("----------")

for value in target1:
    print(value)
print("----------")
print(f'Target 2')
print("----------")
for value in target2:
    print(value)
print()
print(f'Is it empty?: {source.is_empty()}')
