import networkx as nx

def is_iterable_with_len(obj):
    try:
        iter(obj)
        length = len(obj)
        return length > 0
    except (TypeError, ValueError):
        return False

# Example:
G = nx.Graph()
print(is_iterable_with_len(G.nodes))  # True
G.remove_node(list(G.nodes)[0])
print(is_iterable_with_len(G.nodes))  # False
