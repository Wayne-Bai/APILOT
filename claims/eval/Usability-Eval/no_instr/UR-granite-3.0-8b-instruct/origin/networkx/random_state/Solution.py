import networkx as nx
import numpy as np

def decorator(func):
    def wrapper(*args, **kwargs):
        return np.random.RandomState(sum(args) + sum(kwargs.values()))
    return wrapper

@decorator
def generate_graph(num_nodes, num_edges):
    G = nx.erdos_renyi_graph(num_nodes, num_edges / (num_nodes * (num_nodes - 1)))
    return G

# Example usage:
num_nodes = 10
num_edges = 50
G = generate_graph(num_nodes, num_edges)
print(G.nodes())
print(G.edges())
