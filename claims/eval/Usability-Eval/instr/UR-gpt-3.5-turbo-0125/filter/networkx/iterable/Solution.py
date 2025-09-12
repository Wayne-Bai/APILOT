
import networkx as nx

def is_iterable_with_defined_len(obj):
    try:
        len(obj)
        iter(obj)
        return True
    except TypeError:
        return False
    
# Test the function
example_list = [1, 2, 3, 4, 5]
print(is_iterable_with_defined_len(example_list))  # Output: True
