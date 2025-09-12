import networkx as nx

def is_iterable_with_length(obj):
    try:
        len(obj)
        return True
    except TypeError:
        return False

# Example usage:
graph = nx.Graph()
print(is_iterable_with_length(graph))  # True
print(is_iterable_with_length("Hello"))  # True
print(is_iterable_with_length(123))  # False
