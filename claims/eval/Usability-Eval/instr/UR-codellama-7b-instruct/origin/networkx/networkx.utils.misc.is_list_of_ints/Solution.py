import networkx as nx

def is_list_of_ints(lst):
    return all(isinstance(elem, int) for elem in lst)
