"""
------------------------------------------------------------------------
[This program test task four]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-03-23"
------------------------------------------------------------------------
"""
from BST_linked import BST

bst=BST()

for i in range(10):
    bst.insert(i)
    
yes=7
no=44
print(bst.node_counts())
print("Is yes in the BST?")
print(yes in bst)
print("Is no in the BST?")
print(no in bst)
print("BST parent iterative:")
print(bst.parent(yes))
print("BST parent recursive:")
print(bst.parent_r(yes))
