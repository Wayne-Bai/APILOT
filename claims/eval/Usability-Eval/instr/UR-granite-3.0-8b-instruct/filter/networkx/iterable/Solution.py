import networkx as nx

def is_iterable_with_len(obj):
    try:
        len(obj)
        return True
    except TypeError:
        return False

# Example usage:
graph = nx.Graph()
print(is_iterable_with_len(graph))  # Output: True
print(is_iterable_with_len(123))    # Output: False
