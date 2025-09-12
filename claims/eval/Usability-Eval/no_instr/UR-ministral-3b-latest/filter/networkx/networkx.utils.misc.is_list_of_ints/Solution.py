import networkx as nx

def is_list_of_ints(lst):
    return all(isinstance(i, int) for i in lst)

# Sample usage
print(is_list_of_ints([]))          # should return False
print(is_list_of_ints([1, 2, 3]))   # should return True
print(is_list_of_ints([1, '2', 3])) # should return False
print(is_list_of_ints([1.5, 2, 3])) # should return False
