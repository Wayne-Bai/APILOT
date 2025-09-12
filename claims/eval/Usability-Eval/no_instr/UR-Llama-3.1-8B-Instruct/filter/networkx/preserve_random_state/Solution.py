import numpy as np
import networkx as nx

# Define a decorator to preserve the numpy random state
def preserve_random_state(func):
    """
    A decorator to preserve the numpy random state during a function execution.
    
    Args:
        func: The function for which the numpy random state needs to be preserved.
    
    Returns:
        wrapper: The wrapper function that preserves the numpy random state.
    """
    def wrapper(*args, **kwargs):
        # Get the current numpy random state
        state = np.random.get_state()
        
        try:
            # Execute the original function
            return func(*args, **kwargs)
        finally:
            # Restore the original numpy random state
            np.random.set_state(state)
    return wrapper

# Example usage:
@preserve_random_state
def generate_random_network(num_nodes, num_edges):
    """
    Generate a random graph with the given number of nodes and edges.
    
    Args:
        num_nodes (int): The number of nodes in the graph.
        num_edges (int): The number of edges in the graph.
    
    Returns:
        G (nx.Graph): The generated random graph.
    """
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    for _ in range(num_edges):
        u, v = np.random.choice(num_nodes, 2, replace=False)
        G.add_edge(u, v)
    return G

# Generate a random graph with 10 nodes and 5 edges
G = generate_random_network(10, 5)
print(G.edges)
