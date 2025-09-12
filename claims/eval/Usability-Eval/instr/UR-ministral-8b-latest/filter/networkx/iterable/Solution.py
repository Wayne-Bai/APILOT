import networkx as nx

def is_iterable_with_len(obj):
    try:
        iter(obj)
        return len(obj) is not None
    except TypeError:
        return False

# Example usage:
# G = nx.Graph()
# print(is_iterable_with_len(G))  # Should return True
