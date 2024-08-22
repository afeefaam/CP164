"""
------------------------------------------------------------------------
[This program is tests the priority q with a file]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-25"
------------------------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
from utilities import priority_queue_test
fh="foods.txt"

with open(fh, "r") as file:
    file=[line.strip() for line in file]
q=Priority_Queue()

q.insert(file)
priority_queue_test(q)

for value in q:
    print(value)
