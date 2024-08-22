"""
------------------------------------------------------------------------
[This program contains all of the functions]
------------------------------------------------------------------------
Author: Afeefa Malik
ID:     169060299
Email:  mali0299@mylaurier.ca
__updated__ ="2024-02-03"
------------------------------------------------------------------------
"""
from queue import Queue
from Priority_Queue_array import Priority_Queue

def queue_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source queue into separate target queues with values
    alternating into the targets. At finish source queue is empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target1, target2 = queue_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - a queue (Queue)
    Returns:
        target1 - contains alternating values from source (Queue)
        target2 - contains other alternating values from source (Queue)
    -------------------------------------------------------
    """
    target1=Queue()
    target2=Queue()
    while not source.is_empty():
        current_value=source.remove()
        target1.insert(current_value)
        
        if not source.is_empty():
            current_value=source.remove()
            target2.insert(current_value)
            
    return target1, target2
    
def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1=Priority_Queue()
    target2=Priority_Queue()
    while not source.is_empty() and source.peek()>key:
        current_value=source.remove()
        target1.insert(current_value)
        
        if not source.is_empty() and source.peek()<=key:
            current_value=source.remove()
            target2.insert(current_value)
            
    return target1, target2
    
