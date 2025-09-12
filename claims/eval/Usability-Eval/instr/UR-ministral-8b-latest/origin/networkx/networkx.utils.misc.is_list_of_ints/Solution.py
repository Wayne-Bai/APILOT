import networkx as nx

def is_list_of_ints(lst):
    return all(isinstance(x, int) for x in lst)

# Example usage:
example_list = [1, 2, 3, 4, 5]
print(is_list_of_ints(example_list)) # Output: True

example_list = [1, "two", 3, 4, 5]
print(is_list_of_ints(example_list)) # Output: False
