"""
------------------------------------------------------------------------
[This program contains all of the functions for lab 9]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-03-14"
------------------------------------------------------------------------
"""
def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
     695    2 Lasagna, 7
    1355    4 Butter Chicken, 2
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print("Hashes")
    print("Hash    Slot    Key")
    print("----    ----    ---")
    for value in values:
        h=hash(value)
        slot=h%slots
        key_str=str(value)
        print('{:<8}{:<5} {}'.format(h,slot,key_str))
    return

    
    
