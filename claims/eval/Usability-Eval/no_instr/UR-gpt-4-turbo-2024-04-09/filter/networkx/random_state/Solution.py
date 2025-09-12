import networkx as nx
import numpy as np
from functools import wraps

def random_state_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        seed = kwargs.pop('seed', None)
        random_state = np.random.RandomState(seed)
        return func(*args, **kwargs, random_state=random_state)
    return wrapper

@random_state_decorator
def example_networkx_function(random_state, **kwargs):
    G = nx.erdos_renyi_graph(10, 0.5, seed=random_state)
    return nx.adjacency_matrix(G).todense()

# Example usage
result = example_networkx_function(seed=42)
print(result)
