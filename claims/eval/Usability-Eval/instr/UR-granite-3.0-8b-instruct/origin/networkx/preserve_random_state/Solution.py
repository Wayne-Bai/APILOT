import networkx as nx
import numpy as np

def preserve_random_state(func):
    def wrapper(*args, **kwargs):
        np.random.seed(42)  # Set the random seed to preserve the state
        result = func(*args, **kwargs)
        return result
    return wrapper

@preserve_random_state
def generate_random_graph(n, p):
    G = nx.erdos_renyi_graph(n, p)
    return G

# Usage
G = generate_random_graph(100, 0.1)
print(G.nodes())
