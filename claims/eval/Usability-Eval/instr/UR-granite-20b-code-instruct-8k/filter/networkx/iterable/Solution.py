import networkx as nx

def is_iterable_with_len(obj):
    """Return True if obj is iterable with a well-defined len()."""
    try:
        len(obj)
    except TypeError:
        return False
    else:
        return True
