import networkx as nx
import numpy as np
from random import Random
from functools import wraps

# Decorator to generate a numpy.random.RandomState instance
def random_state_decorator(seed=0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            rs = np.random.RandomState(seed)
            return func(rs, *args, **kwargs)
        return wrapper
    return decorator

# Usage example:
@random_state_decorator(seed=42)
def generate_random_graph(rs, num_nodes, num_edges):
    # Generate a random graph
    G = nx.empty_graph(num_nodes)
    nodes = list(G.nodes)
    for _ in range(num_edges):
        while True:
            u = rs.choice(nodes)
            v = rs.choice(nodes)
            if u!= v and not G.has_edge(u, v):
                break
        G.add_edge(u, v)
    return G

# Generate a random graph with 10 nodes and 15 edges
G = generate_random_graph(10, 15)
# Print the graph
print(G.edges)

# Erdos-Renyi random graph
@random_state_decorator(seed=42)
def erdos_renyi_random_graph(rs, n, p):
    return nx.erdos_renyi_graph(n, p, random_state=rs)

# Generate Erdos-Renyi random graph with 10 nodes and 0.3 probability of edge creation
G = erdos_renyi_random_graph(10, 0.3)
# Print the graph
print(G.edges)
