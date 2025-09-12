import networkx as nx

def is_iterator(obj):
    return hasattr(obj, '__iter__')

# Checking if the object is an iterator
print(is_iterator([1, 2, 3]))  # True
print(is_iterator((1, 2, 3)))  # True
print(is_iterator("hello"))  # True
print(is_iterator(123))  # False
