import networkx as nx
import inspect

def is_iterator(obj):
    """
    Returns True if and only if the given object is an iterator object.
    
    Parameters
    ----------
    obj : object
        The object to be checked if it's an iterator.

    Returns
    -------
    bool
        True if the object is an iterator, False otherwise.
    """
    return inspect.isiterator(obj)

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')

# Get the neighbors of node 'A'
neighbors = iter(G.neighbors('A'))

print(is_iterator(neighbors))  # Returns: True
