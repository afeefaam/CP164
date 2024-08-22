"""
------------------------------------------------------------------------
[This program determines data from a matrix]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-13"
------------------------------------------------------------------------
"""

from functions import matrix_stats

a=[[2,3,4],[5,6,7]]

small, large, total, average = matrix_stats(a)

print(small, large, total, average)