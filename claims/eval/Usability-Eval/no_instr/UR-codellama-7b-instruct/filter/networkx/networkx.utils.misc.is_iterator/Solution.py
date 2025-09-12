import networkx as nx

def is_iterator(obj):
    return nx.is_iterable(obj) and not nx.is_collection(obj)
