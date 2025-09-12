import networkx as nx

def is_iterable_with_len(obj):
    try:
        iterator = iter(obj)
        length = len(obj)
        return True
    except (TypeError, AttributeError):
        return False

# Example usage
graph = nx.Graph()
graph.add_nodes_from([1, 2, 3, 4])
result = is_iterable_with_len(graph.nodes())
print(result)  # Output: True

non_iterable_obj = 5
result = is_iterable_with_len(non_iterable_obj)
print(result)  # Output: False
