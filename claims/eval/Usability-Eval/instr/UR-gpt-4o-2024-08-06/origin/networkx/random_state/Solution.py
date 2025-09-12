import networkx as nx
import numpy as np
import functools

def random_state_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Check if a RandomState instance is provided, else create one
        if 'random_state' not in kwargs:
            seed = kwargs.pop('seed', None)
            kwargs['random_state'] = np.random.RandomState(seed)
        return func(*args, **kwargs)
    return wrapper

# Example usage with a function in networkx that can use random_state
@random_state_decorator
def example_function(graph, random_state=None):
    # Here you can use random_state for performing random operations
    random_value = random_state.rand()
    print("Random value:", random_value)

# Example of creating a graph and using the function
G = nx.Graph()
example_function(G)
