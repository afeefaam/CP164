"""
------------------------------------------------------------------------
[This program is tests array to queue,array and test]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-25"
------------------------------------------------------------------------
"""
from Queue_array import Queue
from utilities import array_to_queue
from utilities import queue_to_array
from utilities import queue_test

queue = Queue()
target=[]
a=[100,200,300]
source=[99]

array_to_queue(queue, source)
queue_to_array(queue, target)
queue_test(a)

print(f'Source: {source}')
print(f'Target: {target}')
print(f'a: {a}')
