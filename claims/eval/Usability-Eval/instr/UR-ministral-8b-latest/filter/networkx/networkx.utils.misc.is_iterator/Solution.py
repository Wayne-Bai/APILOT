import networkx as nx

def is_iterator(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

# Example Usage:
G = nx.Graph()
print(is_iterator(G.nodes()))  # True
print(is_iterator(G.edges()))  # True
print(is_iterator(G.nodes.data()))  # False
