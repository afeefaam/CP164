"""
------------------------------------------------------------------------
[This program evaluates a postfix expression]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-27"
------------------------------------------------------------------------
"""
from functions import postfix

string="12 5 -"
print(f'String: {string}')
answer=postfix(string)

print(f'Answer: {answer}')