import numpy as np
import networkx as nx
from functools import wraps

def preserve_random_state(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        state = np.random.get_state()
        try:
            return func(*args, **kwargs)
        finally:
            np.random.set_state(state)
    return wrapper

# Using the decorator
@preserve_random_state
def generate_graph():
    G = nx.gnp_random_graph(100, 0.01)
    # Perform graph operations here.
    return G
