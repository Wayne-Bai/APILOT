import networkx as nx

def is_list_of_ints(lst):
    return all(isinstance(i, int) for i in lst)
