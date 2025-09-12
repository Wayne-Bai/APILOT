import networkx as nx
from collections.abc import Iterable

def is_iterable_with_len(obj):
    """
    Return True if obj is iterable and has a well-defined len().
    
    Parameters:
    obj : object
        Object to check for iterability and len().
        
    Returns:
    bool
        True if obj is iterable and has a well-defined len(), otherwise False.
    """
    return isinstance(obj, Iterable) and hasattr(obj, '__len__')

# Example usage:
example_graph = nx.Graph()
print(is_iterable_with_len(example_graph))  # Output: True
example_list = [1, 2, 3]
print(is_iterable_with_len(example_list))  # Output: True
example_set = {1, 2, 3}
print(is_iterable_with_len(example_set))   # Output: True
example_number = 42
print(is_iterable_with_len(example_number)) # Output: False
