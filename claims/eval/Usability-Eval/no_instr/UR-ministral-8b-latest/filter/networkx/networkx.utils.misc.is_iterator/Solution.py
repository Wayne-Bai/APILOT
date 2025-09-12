import networkx as nx

def is_iterator(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

# Example usage:
object_to_test = (item for item in [1, 2, 3])
print(is_iterator(object_to_test))  # Output: True
