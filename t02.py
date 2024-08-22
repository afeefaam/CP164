"""
------------------------------------------------------------------------
[This program tests task two]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-14"
------------------------------------------------------------------------
"""
from BST_linked import BST
from functions import do_comparisons, fill_bst, comparison_total

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"
bst1=BST()
bst2=BST()
bst3=BST()
fill_bst(bst1, DATA1)
fill_bst(bst2, DATA2)
fill_bst(bst3, DATA3)
file_variable=open("miserables.txt","r",encoding="utf-8")
do_comparisons(file_variable, bst1)
a=comparison_total(bst1)
file_variable=open("miserables.txt","r",encoding="utf-8")
do_comparisons(file_variable, bst2)
b=comparison_total(bst2)
file_variable=open("miserables.txt","r",encoding="utf-8")
do_comparisons(file_variable, bst3)
c=comparison_total(bst3)
print("Comparing by order: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(f"Total Comparisons: {a}")
print("------------------------------------------------------------")
print("Comparing by order: MFTCJPWADHKNRUYBEIGLOQSVXZ")
print(f"Total Comparisons: {b}")
print("------------------------------------------------------------")
print("Comparing by order: ETAOINSHRDLUCMPFYWGBVKJXZQ")
print(f"Total Comparisons: {c}")