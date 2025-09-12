import networkx as nx
import numpy as np

def seed_decorator(func):
    def wrapper(*args, **kwargs):
        seed = kwargs.get('seed', None)
        random_state = np.random.RandomState(seed)
        kwargs['random_state'] = random_state
        return func(*args, **kwargs)
    return wrapper

@seed_decorator
def generate_random_graph(n, p, random_state=None):
    # Generate random graph using the NetworkX library with numpy.random.RandomState for randomness
    random_graph = nx.erdos_renyi_graph(n, p, seed=random_state)
    return random_graph

# Example usage:
# Generates an Erdős-Rényi graph (G(n, p) model) with 10 nodes and a probability of 0.5 for edge creation
graph = generate_random_graph(10, 0.5, seed=42)
print(graph.edges())
