
import networkx as nx

def is_iterable(obj):
    try:
        _ = iter(obj)
        return True
    except TypeError:
        return False
