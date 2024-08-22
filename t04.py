"""
------------------------------------------------------------------------
[This program outputs the food table.]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-20"
------------------------------------------------------------------------
"""

from Food import Food
from Food_utilities import food_table

food=Food("Mango",4,True,23)
food1=Food("Chicken",3,False,349)
food2=Food("Pancakes",1,False,120)
foods=[food,food1,food2]

food_table(foods)
