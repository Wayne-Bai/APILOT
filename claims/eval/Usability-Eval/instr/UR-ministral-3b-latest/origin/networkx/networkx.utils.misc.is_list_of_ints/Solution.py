import networkx as nx

def is_all_integers(lst):
    return all(isinstance(x, int) for x in lst)

# Testing the function
sample_list = [1, 2, 3, 4, 5]
print(is_all_integers(sample_list))  # True

non_integer_list = [1, 2, 'three', 4]
print(is_all_integers(non_integer_list))  # False

empty_list = []
print(is_all_integers(empty_list))  # True
