import networkx as nx
import inspect

def is_iterator(obj):
    """
    Returns True if and only if the given object is an iterator object.

    Args:
        obj (object): The object to check.

    Returns:
        bool: True if the object is an iterator, False otherwise.
    """
    return inspect.isgenerator(obj) or hasattr(obj, '__next__')

# Example usage
G = nx.Graph()
G.add_edge(1, 2, weight=3)
G.add_edge(2, 3, weight=4)

# Check if the edges of the graph are an iterator
edges = nx.edges(G)
print(is_iterator(edges))  # Output: True

# Check if the values returned by the iterator are also iterators
for edge in edges:
    print(is_iterator(nx.neighbors(G, edge[0])))  # Output: True
