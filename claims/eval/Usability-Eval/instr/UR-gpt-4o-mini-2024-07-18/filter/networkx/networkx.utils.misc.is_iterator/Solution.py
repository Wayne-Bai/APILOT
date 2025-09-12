import networkx as nx

def is_iterator(obj):
    """Returns True if and only if the given object is an iterator."""
    return hasattr(obj, '__iter__') and not hasattr(obj, '__len__')

# Example usage
example_list = [1, 2, 3]
example_iterator = iter(example_list)

print(is_iterator(example_list))       # False
print(is_iterator(example_iterator))   # True
