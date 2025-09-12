import networkx as nx
from collections.abc import Iterator

def is_iterator(obj):
    return isinstance(obj, Iterator)

# Example usage:
graph_iter = iter(nx.path_graph(3).nodes)
non_iter = nx.path_graph(3).nodes  # Not an iterator, just a view of nodes

print(is_iterator(graph_iter))  # Should print True
print(is_iterator(non_iter))    # Should print False
