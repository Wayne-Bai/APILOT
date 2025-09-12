import networkx as nx

def is_iterator(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False
