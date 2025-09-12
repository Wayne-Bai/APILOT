import networkx as nx
import numpy as np

def preserve_random_state(func):
    def wrapper(*args, **kwargs):
        original_state = np.random.get_state()
        result = func(*args, **kwargs)
        np.random.set_state(original_state)
        return result
    return wrapper

@preserve_random_state
def generate_random_graph(n, p):
    G = nx.gnm_random_graph(n, int(n * p))
    return G

# Example usage:
n = 10
p = 0.5
G = generate_random_graph(n, p)
