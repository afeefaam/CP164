"""
------------------------------------------------------------------------
[This program tests the Circular Queue]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-02-03"
------------------------------------------------------------------------
"""
from Queue_circular import Queue
from Food import Food

key=Queue()
f1=Food("Lasagna",7,False,135)
f2=Food("Butter Chicken",2,False,490)
f3=Food("Moo Goo Guy Pan",1,False,272)

empty_one=key.is_empty()
full_one=key.is_full()

key.insert(f1)
peeks=key.peek()

key.insert(f2)
length=len(key)

full=key.is_full()
empty_two=key.is_empty()

removed_value=key.remove()
key.insert(f3)

print(f'We need an empty queue, is this queue empty?: \n{empty_one}')
print(f'Just making sure, Is this queue full?: \n{full_one}')
print(f'Lets peek at the value: \n{peeks}')
print(f'The length of the queue is: \n{length}')
print(f'Is this queue full?: \n{full}')
print(f'Is this queue empty?: \n{empty_two}')
print(f'Lets get the removed value: \n{removed_value}')

print("\n----------------")
print("Printed queue:")
print("----------------")
for value in key:
    print(value)
