import networkx as nx
import numpy as np

def set_seed_random_state(seed):
    np.random.seed(seed)

# Wrapper to preserve random state
def random_state_decorator(func):
    def wrapper(*args, **kwargs):
        seed = kwargs.get('random_seed', None)
        if seed is not None:
            np.random.seed(seed)
        result = func(*args, **kwargs)
        return result
    return wrapper

# Example usage:
@random_state_decorator
def create_graph(num_nodes):
    G = nx.erdos_renyi_graph(num_nodes, 0.1)
    return G

# Test the decorator
print(create_graph(num_nodes=10))
