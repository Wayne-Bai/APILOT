import networkx as nx

# Function to check if the object is iterable with a well-defined len
def is_iterable_with_len(obj):
    try:
        len(obj)
        return True
    except TypeError:
        return False

# Example usage
# Test with different types
print(is_iterable_with_len("non_iterable string"))  # Output: False
print(is_iterable_with_len([1, 2, 3]))  # Output: True
print(is_iterable_with_len(nx.Graph()))  # Output: True
print(is_iterable_with_len(iter(a=range(10))))  # Output: True
print(is_iterable_with_len((1, 2, 3)))  # Output: False
