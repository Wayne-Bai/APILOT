import networkx as nx
import numpy as np

def random_state_decorator(func):
    def wrapper(*args, **kwargs):
        rng = np.random.RandomState()
        return func(rng, *args, **kwargs)
    return wrapper

@random_state_decorator
def create_random_graph(rng, num_nodes, probability):
    G = nx.erdos_renyi_graph(num_nodes, probability, random_state=rng)
    return G

# Example usage:
num_nodes = 10
probability = 0.5
random_graph = create_random_graph(num_nodes, probability)
print(random_graph.edges())
