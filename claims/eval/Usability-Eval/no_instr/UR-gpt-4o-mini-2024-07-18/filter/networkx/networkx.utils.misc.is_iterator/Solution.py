import networkx as nx

def is_iterator(obj):
    return hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes))

# Example usage
print(is_iterator(iter([1, 2, 3])))  # True
print(is_iterator([1, 2, 3]))         # False
