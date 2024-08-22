"""
------------------------------------------------------------------------
[This program contains all of the functions]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-01-13"
------------------------------------------------------------------------
"""

def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of value
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    new_list=[]
    for i in values:
        if i not in new_list:
            new_list.append(i)
    return None
    
def list_subtraction(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtraction(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    
    i=0
    while i<len(minuend):
        if minuend[i] in subtrahend:
            minuend.pop(i)
        else:
            i+=1        
    
    return None
def dsmvwl(string):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvwl(string)
    -------------------------------------------------------
    Parameters:
       string - a string (str)
    Returns:
       out - string with the vowels removed (str)
    -------------------------------------------------------
    """
    vowels="aeiouAEIOU"
    out=""
    for char in string:
        if char not in vowels:
            out+=char
    return out
    
        
  
def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged:
    Do not strip() the lines.
    Use: upp, low, dig, whi, rem = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        upp - the number of uppercase letters in the file (int)
        low - the number of lowercase letters in the file (int)
        dig - the number of digits in the file (int)
        whi - the number of whitespace characters in the file (int)
        rem - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    line=fv.readline()
    upp=0
    low=0
    dig=0
    whi=0
    rem=0

    while line!="":
        for char in line:
            if char.isupper():
                upp+=1
            elif char.islower():
                low+=1
            elif char.isdigit():
                dig+=1
            elif char.isspace():
                whi+=1
            
        rem+=len(line)-(upp+low+dig+whi)
        line=fv.readline()
        
    return upp, low, dig, whi, rem
    
def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year=False
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap_year=True
  
        else:
            leap_year=True
    
    return leap_year
    
def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    valid=True
    if name[0].isdigit() or name.iskeyword():
        valid=False
    
    for char in name:
        if not (char.isalpha() or char.isdigit() or char=="_"):
            valid=False
            
    
    return valid
    
def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    md=0
    
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            diff=a[i]-a[i+1]
        else:
            diff=a[i+1]-a[i]

        if diff>md:
            md=diff
    return md
    
    
def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    count=0
    small=a[0][0]
    large=0
    total=a[0][0]
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            element=a[i][j] 
            
            if element<small: 
                small=element
            elif element>large:
                large=element
            total+=element
            count+=len(a[i])
    average=total/count
    return small, large, total, average
        
    
def matrixes_add(a, b):
    """
    -------------------------------------------------------
    Sums the contents of matrixes a and b. a and b must have
    the same number of rows and columns.
    a and b must be unchanged.
    Use: c = matrixes_add(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix sum of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    assert len(a) == len(b) and len(a[0]) == len(b[0])
    
    rows=len(a)
    cols=len(a[0])
    c=[]
    for num in range(rows):
        c.append([0]*cols)
    for i in range(rows):
        for j in range(cols):
            c[i][j]=a[i][j]+b[i][j]
    return c
            
            