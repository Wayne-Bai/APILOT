import networkx as nx

def is_iterable(obj):
    """
    Returns True if obj is iterable with a well-defined len().
    
    Args:
    obj: The object to check for iterability and well-defined len().
    
    Returns:
    bool: True if obj is iterable with a well-defined len(), False otherwise.
    """
    try:
        # Check if obj has a well-defined len()
        len(obj)
        
        # Check if obj is iterable
        iter(obj)
        
        return True
    
    except TypeError:
        return False


# Example usage:
G = nx.Graph()

# Add nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Add edges
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

print(is_iterable(G.nodes))  # True
print(is_iterable(G.edges))  # True
print(is_iterable(G.neighbors(1)))  # True
