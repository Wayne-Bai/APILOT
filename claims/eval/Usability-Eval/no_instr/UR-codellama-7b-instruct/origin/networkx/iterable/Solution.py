
import networkx as nx

def check_iterable(obj):
    try:
        _ = len(obj)
        return True
    except TypeError:
        return False
