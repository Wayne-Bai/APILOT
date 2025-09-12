import networkx as nx
import numpy as np

def random_state_decorator(func):
    def wrapper(*args, **kwargs):
        random_state = np.random.RandomState(kwargs.get('seed', 0))
        result = func(*args, random_state=random_state, **kwargs)
        return result
    return wrapper

@random_state_decorator
def generate_graph(n_nodes, seed=0):
    G = nx.Graph()
    G.generate_from_random_state(n_nodes, seed=seed)
    return G
