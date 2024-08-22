"""
------------------------------------------------------------------------
[This program solves a maze using Depth-first search.]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-27"
------------------------------------------------------------------------
"""
from functions import stack_maze

maze={
    'Start':['A', 'B'],
    'A':['c', 'D'],
    'B':['E', 'F'],
    'C':['X'],
    'D':['G'],
    'E':['X'],
    'F':['H'],
    'G':['X'],
    'H':['X'],
    'X':[]
    }

print(f'Maze: {maze}')
path=stack_maze(maze)

print(f'Path: {path}')
