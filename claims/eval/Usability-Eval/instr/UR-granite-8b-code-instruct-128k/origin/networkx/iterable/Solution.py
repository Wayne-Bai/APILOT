
import networkx as nx

def check_iterable_with_len(obj):
    try:
        iter(obj)
        len(obj)
        return True
    except TypeError:
        return False
