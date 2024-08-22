"""
-------------------------------------------------------
[This program writes content to a new file]
-------------------------------------------------------
Author:  Afeefa Malik 
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""

from Food_utilities import write_foods

from Food import Food

file_variable=open("foods_write.txt", "w", encoding="utf-8")

food1=Food("Biryani", 2, False, 567)
foods=[]
foods.append(food1)

write_foods(file_variable, foods)

    
file_variable.close()

