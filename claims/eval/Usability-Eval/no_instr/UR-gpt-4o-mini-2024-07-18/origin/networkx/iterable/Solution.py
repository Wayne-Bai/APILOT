import networkx as nx

def is_iterable_with_len(obj):
    return isinstance(obj, (list, tuple, dict, set, str)) and hasattr(obj, '__len__')

# Example usage:
example_list = [1, 2, 3]
example_string = "Hello"
example_integer = 5

print(is_iterable_with_len(example_list))  # True
print(is_iterable_with_len(example_string))  # True
print(is_iterable_with_len(example_integer))  # False
