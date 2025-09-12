import networkx as nx
import numpy as np

def random_state_decorator(func):
    def wrapper(*args, **kwargs):
        random_state = np.random.RandomState()
        return func(random_state, *args, **kwargs)
    return wrapper

@random_state_decorator
def generate_random_graph(random_state, num_nodes, edge_prob):
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    for u in range(num_nodes):
        for v in range(u + 1, num_nodes):
            if random_state.rand() < edge_prob:
                G.add_edge(u, v)
    return G

# Example usage
random_graph = generate_random_graph(num_nodes=10, edge_prob=0.3)
print(random_graph.edges())
