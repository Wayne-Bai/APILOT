
# Importing required library
import networkx as nx

def is_iterator(obj):
    # Check if object has __iter__ and next methods
    return hasattr(obj, '__iter__') and hasattr(obj, '__next__')

# Test the function
obj = iter([1, 2, 3])
print(is_iterator(obj))  # Output: True

obj = [1, 2, 3]
print(is_iterator(obj))  # Output: False
