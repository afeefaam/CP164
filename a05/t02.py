"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-14"
------------------------------------------------------------------------
"""
from Sorted_List_array import Sorted_List

a1=Sorted_List()
for i in range(6):
    a1.insert(i)
print(a1._values,a1.find(3),a1.index(3))
print("----------------------")
a2=Sorted_List()
target=Sorted_List()
for i in range(7):
    a2.insert(i)
target.intersection(a1, a2)
print(a2._values,target._values)
print("----------------------------------------")

target1, target2=target.split_key(4)
print(target1._values,target2._values)
print("----------")
