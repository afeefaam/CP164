"""
------------------------------------------------------------------------
[This program tests the priority queue]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-02-17"
------------------------------------------------------------------------
"""

from Priority_Queue_linked import Priority_Queue

pq=Priority_Queue()

pq.insert("a")
pq.insert("f")
pq.insert("e")

print(f'Front: {pq._front._value}')
print(f'Length?: {pq._count}')
