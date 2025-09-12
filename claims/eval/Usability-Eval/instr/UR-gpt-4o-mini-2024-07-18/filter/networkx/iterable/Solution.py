import networkx as nx

def is_iterable_with_length(obj):
    return hasattr(obj, '__iter__') and hasattr(obj, '__len__')

# Example usage:
print(is_iterable_with_length([1, 2, 3]))  # True
print(is_iterable_with_length("Hello"))     # True
print(is_iterable_with_length(10))          # False
print(is_iterable_with_length({'a': 1}))    # True
