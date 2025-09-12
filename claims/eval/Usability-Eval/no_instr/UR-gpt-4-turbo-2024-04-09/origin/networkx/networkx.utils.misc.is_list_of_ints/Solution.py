import networkx as nx

def is_list_of_ints(lst):
    return all(isinstance(item, int) for item in lst)
