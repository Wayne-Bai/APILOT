import numpy as np
import networkx as nx

def random_state_generator(func):
    def wrapper(*args, **kwargs):
        # Create a random seed from the function name
        seed = abs(hash(func.__name__)) % (10 ** 8)
        np.random.seed(seed)

        # Generate a random graph
        G = nx.gnp_random_graph(10, 0.3, seed)

        # Execute the function with the generated random state
        return func(G, *args, **kwargs)
    return wrapper

@random_state_generator
def example_function(graph, *args, **kwargs):
    # This function will now receive a randomly generated graph as its first argument
    pass
