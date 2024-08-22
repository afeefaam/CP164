"""
------------------------------------------------------------------------
[This program tests array to queue and queue test]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-25"
------------------------------------------------------------------------
"""
from Queue_array import Queue
from utilities import array_to_queue
from utilities import queue_test

a=[4,6,7,2,4]
q=Queue()
array_to_queue(q,a)
queue_test(a)

