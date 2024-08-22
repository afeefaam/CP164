"""
------------------------------------------------------------------------
[This program ouputs the by origin function]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-20"
------------------------------------------------------------------------
"""
from Food_utilities import by_origin
from Food import Food


food=Food("Yogurt",2,False,92)
food1=Food("Chicken",3,False,220)
food2=Food("Banana",1,True,56)
foods=[food,food1,food2]

o_foods = by_origin(foods, 1)


for i in o_foods:
    print(i)


