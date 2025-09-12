import networkx as nx
import numpy as np

def random_state_decorator(func):
    """
    A decorator to generate a numpy.random.RandomState instance.
    
    Args:
    func: The function to be decorated.
    
    Returns:
    A wrapper function that generates a RandomState instance before calling the original function.
    """
    def wrapper(*args, **kwargs):
        # Generate a RandomState instance
        random_state = np.random.default_rng()
        
        # Call the original function with the generated RandomState instance
        return func(random_state, *args, **kwargs)
    
    return wrapper

# Example usage:
@random_state_decorator
def generate_random_graph(random_state, num_nodes, probability):
    """
    Generate a random graph with the specified number of nodes and edge probability.
    
    Args:
    random_state: A numpy.random.RandomState instance.
    num_nodes: The number of nodes in the graph.
    probability: The probability of an edge existing between any two nodes.
    
    Returns:
    A NetworkX graph object.
    """
    G = nx.gnp_random_graph(num_nodes, probability, random_state=random_state)
    return G

# Generate a random graph with 10 nodes and 0.5 edge probability
random_graph = generate_random_graph(10, 0.5)
print(nx.info(random_graph))
