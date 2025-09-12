import networkx as nx

def is_iterator(obj):
    try:
        next(obj)
        return True
    except StopIteration:
        return False

# Example usage:
# If you want to check if some object (like a generator, iterator, or list) is iterable
obj = [1, 2, 3]
print(is_iterator(obj))  # Should print True

obj = (1, 2, 3)
print(is_iterator(obj))  # Should print True
