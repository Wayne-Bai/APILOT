import networkx as nx

def is_iterable_with_len(obj):
    try:
        iter(obj)
        len(obj)
        return True
    except TypeError:
        return False

# Example usage:
# G = nx.Graph()
# print(is_iterable_with_len(G.nodes()))  # Should return True
