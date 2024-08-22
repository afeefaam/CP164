"""
------------------------------------------------------------------------
[This program get a new list from an old one]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-02-08"
------------------------------------------------------------------------
"""
from functions import bag_to_set

bag=[4, 5, 3, 4, 5, 2, 2, 4]

new_set = bag_to_set(bag)

print(f'Old set: {bag}')
print(f'New set: {new_set}')