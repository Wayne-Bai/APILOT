
import networkx as nx
import collections.abc

def is_iterable(obj):
    # Check if obj has a well-defined len()
    if not hasattr(obj, '__len__'):
        return False

    # Check if obj is iterable
    if not isinstance(obj, collections.abc.Iterable):
        return False

    return True


# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])  # Create a cycle graph

# Check if G is iterable
print(is_iterable(G))  # Output: True

# Check if G.nodes is iterable
print(is_iterable(G.nodes()))  # Output: True

# Check if G.edges is iterable
print(is_iterable(G.edges()))  # Output: True

# Check if string is iterable
print(is_iterable("string"))  # Output: True

# Check if integer is iterable
print(is_iterable(10))  # Output: False
