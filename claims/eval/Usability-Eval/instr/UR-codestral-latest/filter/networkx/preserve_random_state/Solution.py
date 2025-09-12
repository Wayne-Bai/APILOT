import networkx as nx
import numpy as np
import contextlib

@contextlib.contextmanager
def preserve_random_state():
    state = np.random.get_state()
    try:
        yield
    finally:
        np.random.set_state(state)

def your_function(graph):
    with preserve_random_state():
        # Your code that uses np.random here
        pass

# Create a graph
G = nx.Graph()
G.add_edge(1, 2)

# Call your function with the graph
your_function(G)
