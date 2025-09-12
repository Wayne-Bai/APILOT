import networkx as nx
import numpy as np
from functools import wraps

def with_random_state(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Fetch seed if specified, if not use None
        seed = kwargs.pop('seed', None)
        
        # Create a RandomState instance using the seed
        random_state = np.random.RandomState(seed)

        # Execute the function with the generated RandomState instance
        return func(random_state=random_state, *args, **kwargs)
    
    return wrapper

@with_random_state
def example_graph(random_state, nodes=10, probability=0.5):
    # Generate a random graph using the provided random state
    G = nx.generators.fast_gnp_random_graph(nodes, probability, seed=random_state)
    return G

# Use the decorated function
graph = example_graph(seed=42)
print(nx.info(graph))
