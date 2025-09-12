
import networkx as nx
import numpy as np

@nx.decorators.instance_of(np.random.RandomState)
def random_state():
    return np.random.RandomState()

# Example usage
with random_state() as rng:
    print(rng.uniform(0, 1))
