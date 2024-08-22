"""
------------------------------------------------------------------------
[This program contains all of the functions]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-27"
------------------------------------------------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack
import operator

def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target=Stack()
    while not source1.is_empty() and not source2.is_empty():
        target.push(source1.pop())
        target.push(source2.pop())
    
    while not source1.is_empty():
        target.push(source1.pop())
    
    while not source2.is_empty():
        target.push(source2.pop())
        
    return target
    
def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    list=[]
    while not source.is_empty():
        list.append(source.pop())
        
    for value in list:
        source.push(value)
    return
    
def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    is_Palindrome=True
    stack=Stack()
    letters=[]
    for char in string:
        if char.isalpha() or char.isspace():
            letters.append(char.lower())
    
    for char in letters:
        stack.push(char)
        
    for letter in letters:
        if letter !=stack.pop():
            is_Palindrome=False
            
        
    return is_Palindrome 
    
    
# Constants

OPERATORS = "+-*/"
OPS={
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv
    }
    
def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack=Stack()
    for char in string.split(" "):
        if char.isdigit() or (char[0]=='-' and char[1:].isdigit()):
            stack.push(float(char))
        elif char in OPERATORS:
            right=stack.pop()
            left=stack.pop()
            stack.push(OPS[char](left, right))
    answer=stack.pop()
    
    return answer

def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """
    stack=Stack()
    maze['Start'].reverse()
    array_to_stack(stack, maze['Start'])
    pt=stack.pop()
    path=[pt]
    while pt!='X':
        for branch in maze[pt]:
            if branch not in path:
                stack.push(branch)
        if stack.is_empty():
            break 
        pt=stack.pop()
        path.append(pt)
        
    if pt!='X':       
        path=None
            
    return path 


OPERATORS = "+-*/"
OPS={
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv
    }
