"""
-------------------------------------------------------
[This program outputs the vegetarian function]
-------------------------------------------------------
Author:  Afeefa Malik 
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
from Food_utilities import get_vegetarian

from Food import Food

file_variable=open("foods.txt", "r", encoding="utf-8")

foods=[
    Food("Apple", 1, True, 95),
    Food("Chicken", 2, False, 250)
    ]
food=get_vegetarian(foods)

for food in foods:
    print(food)

    
file_variable.close()

