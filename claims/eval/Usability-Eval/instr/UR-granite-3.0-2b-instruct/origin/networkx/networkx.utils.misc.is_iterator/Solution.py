import networkx as nx

def is_iterator(obj):
    return hasattr(obj, '__iter__')

# Test the function
G = nx.Graph()
iter_obj = iter(G.nodes())
print(is_iterator(iter_obj))  # Returns True
