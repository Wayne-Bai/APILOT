import networkx as nx

def is_iterable(obj):
    """Return True if obj is iterable with a well-defined len()."""
    try:
        len(obj)
    except TypeError:
        return False
    else:
        return hasattr(obj, '__len__') and callable(getattr(obj, '__len__', None))
