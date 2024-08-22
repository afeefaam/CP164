"""
------------------------------------------------------------------------
[This program tests the list implementation]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-02-02"
------------------------------------------------------------------------
"""

from List_array import List
from utilities import list_test


file=open("foods.txt", "r")
source=[]

i=0
while i<=(10):
    source.append(file.readline())
    
list_test(source)
