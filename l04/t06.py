"""
------------------------------------------------------------------------
[This program converts an array to list and a list to array]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-02-02"
------------------------------------------------------------------------
"""
from List_array import List
from utilities import array_to_list
from utilities import list_to_array

source=[1,2,3,4,5,6]
llist=List()

array_to_list(llist, source)
print(f'Array to List:')
for value in llist:
    print(value)
llist=List()
for i in range(1,10): 
    llist.append(i)
target=[]    
list_to_array(llist, target)
print(f'List to Array:')
print(target)
