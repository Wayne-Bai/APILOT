import networkx as nx

def is_list_of_ints(lst):
    return isinstance(lst, list) and all(isinstance(i, int) for i in lst)

# Example usage
example_list = [1, 2, 3, 4]
result = is_list_of_ints(example_list)
print(result)  # Output: True
