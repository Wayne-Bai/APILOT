import networkx as nx

my_list = [1, 2, 3, 4, 5]

def is_list_of_ints(lst):
    return all(isinstance(item, int) for item in lst)

result = is_list_of_ints(my_list)
print(result)
