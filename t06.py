"""
------------------------------------------------------------------------
[This program is testing array to pq, array and the queue test]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-25"
------------------------------------------------------------------------
"""
from utilities import array_to_pq
from utilities import pq_to_array
from utilities import priority_queue_test
from Priority_Queue_array import Priority_Queue

target=[4,5,6]
source=[3,4,5]
pq = Priority_Queue()

array_to_pq(pq, source)
pq_to_array(pq, target)
priority_queue_test(pq)

print(f'Target: {target}')
