"""
------------------------------------------------------------------------
[This program tests task three]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-14"
------------------------------------------------------------------------
"""
from BST_linked import BST
from functions import fill_bst, letter_table, do_comparisons, comparison_total
DATA3="ETAOINSHRDLUCMPFYWGBVKJXZQ"
bst=BST()
fill_bst(bst, DATA3)
file_variable=open("miserables.txt", "r",encoding="utf-8")
do_comparisons(file_variable, bst)
test=comparison_total(bst)
letter_table(bst)