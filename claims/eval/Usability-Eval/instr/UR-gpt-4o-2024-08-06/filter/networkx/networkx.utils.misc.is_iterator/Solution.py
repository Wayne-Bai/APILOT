import networkx as nx
from collections.abc import Iterator

def is_iterator(obj):
    """
    Returns True if the given object is an iterator, False otherwise.
    """
    return isinstance(obj, Iterator)

# Example usage:
# some_object = iter([1, 2, 3])
# print(is_iterator(some_object))  # Should return True
# not_an_iterator = [1, 2, 3]
# print(is_iterator(not_an_iterator))  # Should return False
