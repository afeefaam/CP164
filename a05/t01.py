"""
------------------------------------------------------------------------
[This program tests task 1]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-02-10"
------------------------------------------------------------------------
"""
from utilities import array_to_list
from List_array import List 

llist=List()
source=[1,2,3,4,5,6,9,2,1]
array_to_list(llist, source)

llist.clean()
print(llist._values)
print('---------------------')
target=List()
source1=[1,2,3,4,5,6,7,8]
source2=List()
array_to_list(source2, source1)

target.combine(llist,source2)
print(target._values)
print('---------------------------------------------')
target1, target2 = target.split()
print(target1._values,target2._values)
print('----------------------------------------------')
union=List()
list1=List()
array_to_list(list1, [1,2,3,4,5,6,7])

union.union(list1, target1)
print(list1._values,target1._values,union._values)
print('--------------------------------------------------------')
