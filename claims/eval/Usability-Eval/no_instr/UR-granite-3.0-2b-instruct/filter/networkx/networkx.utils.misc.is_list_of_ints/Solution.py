import networkx as nx

def is_list_of_ints(lst):
    return all(isinstance(i, int) for i in lst)

# Test the function
print(is_list_of_ints([1, 2, 3, 4, 5]))  # True
print(is_list_of_ints([1, 2, 'a', 4, 5]))  # False
