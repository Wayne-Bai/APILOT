import networkx as nx
from collections.abc import Iterator

def is_networkx_iterator(obj):
    return isinstance(obj, Iterator)

# Example usage:
G = nx.Graph()
it = iter(G.nodes())
print(is_networkx_iterator(it))  # Should return True if it is an iterator, otherwise False
