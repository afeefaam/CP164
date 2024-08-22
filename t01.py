"""
------------------------------------------------------------------------
[This program tests the linked queue]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-02-17"
------------------------------------------------------------------------
"""
from Queue_linked import Queue

q=Queue()

for i in range(6):
    q.insert(i)
    
print(f'Front: {q._front._value}')
print(f'Rear: {q._rear._value}')
print(f'Is it empty?: {q.is_empty()}')
