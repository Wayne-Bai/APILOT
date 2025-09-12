import networkx as nx

def is_list_of_ints(lst):
    return isinstance(lst, list) and all(isinstance(x, int) for x in lst)
