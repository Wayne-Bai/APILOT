import networkx as nx

def is_iterator(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

# Example usage:
# G = nx.Graph()
# print(is_iterator(G.nodes()))  # Should return True if G.nodes() is an iterator
