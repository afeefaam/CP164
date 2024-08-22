"""
------------------------------------------------------------------------
[This program test task two]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-03-23"
------------------------------------------------------------------------
"""
from functions import insert_words, comparison_total
from Hash_Set_sorted import Hash_Set

fv = open('otoos610.txt', 'r')
hash_set = Hash_Set(26)

insert_words(fv, hash_set)
total, max_word = comparison_total(hash_set)

print("Using array-based list Hash_Set")
print()
print("Total Comparisons: {:,}".format(total))
print("Word with maximum comparisons '{}': {:,}".format(max_word.word, max_word.comparisons))