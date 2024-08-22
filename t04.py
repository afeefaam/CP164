"""
------------------------------------------------------------------------
[This program analyzes a file and outputs specific data]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-13"
------------------------------------------------------------------------
"""

from functions import file_analyze

fv=open("names.txt", 'r',encoding='utf-8')

upp, low, dig, whi, rem = file_analyze(fv)

print(upp, low, dig, whi, rem) 

fv.close()