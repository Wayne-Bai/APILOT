import networkx as nx

def is_list_of_ints(lst):
    return isinstance(lst, list) and all(isinstance(x, int) for x in lst)

# Example usage:
example_list = [1, 2, 3, 4]
result = is_list_of_ints(example_list)
print(f"Is the list a list of integers? {result}")
