"""
------------------------------------------------------------------------
[This program outputs the average calories]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-20"
------------------------------------------------------------------------
"""

from Food import Food
from Food_utilities import average_calories

food=Food("Mango",2,False,390)
food1=Food("Pasta",3,True,20)
food2=Food("Soup",1,True,300)
foods=[food,food1,food2]

avg = average_calories(foods)

print(avg)