import numpy as np
import networkx as nx
from functools import wraps

def preserve_random_state(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        np.random.set_state(np.random._state)
        result = func(*args, **kwargs)
        np.random.set_state(np.random._state)
        return result
    return wrapper

def generate_graph(n_nodes, n_edges):
    G = nx.Graph()
    np.random.seed(0)
    for i in range(n_edges):
        u, v = np.random.randint(0, n_nodes, 2)
        G.add_edge(u, v)
    return G

@preserve_random_state
def decorate_graph(G):
    # Add your decoration logic here
    pass

G = generate_graph(10, 20)
decorate_graph(G)
