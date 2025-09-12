import networkx as nx
import numpy as np

class RandomStateDecorator:
    """
    A decorator that generates a numpy.random.RandomState instance
    with a given seed value.

    Args:
        seed (int): The seed value to use for the random state.

    Returns:
        callable: A function that returns a numpy.random.RandomState instance.
    """
    def __init__(self, seed):
        self.seed = seed

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            rng = np.random.default_rng(self.seed)
            return func(rng, *args, **kwargs)
        return wrapper

# Example usage
@RandomStateDecorator(42)
def generate_random_graph(rng):
    """
    Generate a random graph with 10 nodes and 50 edges.

    Args:
        rng (numpy.random.RandomState): The random state instance to use.

    Returns:
        networkx.Graph: A random undirected graph.
    """
    G = nx.gnm_random_graph(10, 50, seed = 42)
    return G

random_graph = generate_random_graph()
print(random_graph)
