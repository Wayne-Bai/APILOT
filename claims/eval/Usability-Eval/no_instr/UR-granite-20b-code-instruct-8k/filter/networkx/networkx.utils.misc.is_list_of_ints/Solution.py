import networkx as nx

def is_list_of_ints(lst):
    if not isinstance(lst, list):
        return False
    for item in lst:
        if not isinstance(item, int):
            return False
    return True
