import networkx as nx

def is_iterable_with_len(obj):
    return hasattr(obj, '__len__') and callable(obj.__len__)

# Test the function
print(is_iterable_with_len([1, 2, 3]))  # True
print(is_iterable_with_len((1, 2, 3)))  # True
print(is_iterable_with_len({'a': 1, 'b': 2}))  # True
print(is_iterable_with_len(123))  # False
