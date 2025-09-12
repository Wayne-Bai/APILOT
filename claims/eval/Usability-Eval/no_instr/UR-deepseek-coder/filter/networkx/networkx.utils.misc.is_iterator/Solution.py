import networkx as nx

def is_iterator(obj):
    return hasattr(obj, '__iter__') and hasattr(obj, '__next__')

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3)])

# Check if the edges iterator is an iterator object
edges_iterator = iter(G.edges())
print(is_iterator(edges_iterator))  # Output: True
