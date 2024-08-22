"""
-------------------------------------------------------
[This program reads content from a file]
-------------------------------------------------------
Author:  Afeefa Malik 
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""

from Food_utilities import read_foods

file_variable=open("foods.txt", "r", encoding="utf-8")

foods = read_foods(file_variable)

for food in foods:
    print(food)
    
file_variable.close()
