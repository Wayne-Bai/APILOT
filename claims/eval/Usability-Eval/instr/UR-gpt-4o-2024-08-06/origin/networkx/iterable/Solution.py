import networkx as nx

def is_iterable_with_len(obj):
    try:
        iter(obj)
        length = len(obj)
        return True
    except TypeError:
        return False

# Example usages:
example_graph = nx.Graph()
example_graph.add_edges_from([(1, 2), (2, 3), (3, 4)])

print(is_iterable_with_len(example_graph.nodes()))  # Returns True
print(is_iterable_with_len(example_graph.edges()))  # Returns True
print(is_iterable_with_len(123))  # Returns False
print(is_iterable_with_len("hello"))  # Returns True
print(is_iterable_with_len(["a", "b", "c"]))  # Returns True
