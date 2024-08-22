"""
------------------------------------------------------------------------
[This program outputs the food search function]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-20"
------------------------------------------------------------------------
"""
from Food import Food
from Food_utilities import food_search

food=Food("Mango",4,True,23)
food1=Food("Chicken",3,False,349)
food2=Food("Pancakes",1,False,120)
foods=[food,food1,food2]

results = food_search(foods, 2, 560, False)
for i in results:
    print(i)