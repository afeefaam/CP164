"""
------------------------------------------------------------------------
[This program tests the calories by origin function]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-20"
------------------------------------------------------------------------
"""
from Food import Food
from Food_utilities import calories_by_origin

food=Food("Orange",2,True,23)
food1=Food("Apple",3,False,23)
food2=Food("Banana",1,True,23)
foods=[food,food1,food2]

by_origin = calories_by_origin(foods, 2)
print(by_origin)