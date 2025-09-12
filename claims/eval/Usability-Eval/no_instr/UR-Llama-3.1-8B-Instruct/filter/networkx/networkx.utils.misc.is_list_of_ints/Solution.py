import networkx as nx
import numpy as np

def is_list_of_ints(lst):
    """
    Returns True if the list contains only integers.
    
    Parameters:
    lst (list): The list to check.
    
    Returns:
    bool: True if the list contains only integers, False otherwise.
    """
    for item in lst:
        if not isinstance(item, int):
            return False
    return True

# Test the function
print(is_list_of_ints([1, 2, 3]))  # True
print(is_list_of_ints([1, 2, 'a']))  # False
print(is_list_of_ints([]))  # True
print(is_list_of_ints([1, None, 3]))  # False
