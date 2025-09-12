import networkx as nx
import numpy as np
from functools import wraps

# Decorator to preserve the numpy.random state
def preserve_random_state(func):
    """Preserve numpy.random state during function call."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Save current numpy.random state
        state = np.random.get_state()
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Restore numpy.random state
        np.random.set_state(state)
        
        return result
    
    return wrapper


# Example usage:

# Create a new directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# Define a function with the decorator to shuffle nodes
@preserve_random_state
def shuffle_nodes(G):
    # Shuffle the nodes of the graph
    nodes = list(G.nodes)
    np.random.shuffle(nodes)
    
    # Create a new graph with the shuffled nodes
    new_G = nx.DiGraph()
    for u, v in zip(nodes, nodes[1:] + nodes[:1]):
        new_G.add_edge(u, v)
    
    return new_G

# Test the function
new_G = shuffle_nodes(G)

# Print the original graph edges
print("Original graph edges:")
print(list(G.edges))

# Print the new graph edges
print("New graph edges:")
print(list(new_G.edges))
