import networkx as nx
import numpy as np
from functools import wraps

# Create a decorator to preserve the numpy.random state
def preserve_random_state(func):
    """
    Decorator to preserve the numpy.random state during a function.
    
    Parameters:
    func (function): function to be decorated
    
    Returns:
    function: decorated function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        np_state = np.random.get_state()
        result = func(*args, **kwargs)
        np.random.set_state(np_state)
        return result
    return wrapper

# Test the decorator
@preserve_random_state
def test_function():
    G = nx.gnp_random_graph(10, 0.5)
    np.random.shuffle(G.nodes)
    return G

# Generate a graph
G = nx.gnp_random_graph(10, 0.5)

# Print the nodes before calling the test function
print("Nodes before calling test_function:")
print(G.nodes)

# Call the test function
G_test = test_function()

# Print the nodes after calling the test function
print("\nNodes after calling test_function:")
print(G.nodes)
