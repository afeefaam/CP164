"""
------------------------------------------------------------------------
[This program determines whether two queues are equal]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-02-03"
------------------------------------------------------------------------
"""
from Queue_array import Queue

target=Queue()
for i in range(5):
    target.insert(i)
source=Queue()
for i in range(3):
    source.insert(i)
equals = source == target
equals2 = target == target

print("--------")
print("Queue 1:")
print("--------")
for value in target:
    print(value)
print("--------")
print("Queue 2:")
print("--------")
for value in source:
    print(value)
print()
print(f'Is Queue 1 equal to Queue 2?: {equals}')
print(f'Is Queue 1 equal to Queue 1?: {equals2}')
