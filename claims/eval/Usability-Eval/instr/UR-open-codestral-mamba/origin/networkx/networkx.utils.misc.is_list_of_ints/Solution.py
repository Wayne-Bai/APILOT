import networkx as nx

def is_list_of_ints(lst):
    return all(isinstance(i, int) for i in lst)

# Testing the function
print(is_list_of_ints([1, 2, 3, 4, 5]))
print(is_list_of_ints(['a', 'b', 'c']))
