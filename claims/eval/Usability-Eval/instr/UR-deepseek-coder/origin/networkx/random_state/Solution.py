import networkx as nx
import numpy as np

def random_state_decorator(func):
    def wrapper(*args, **kwargs):
        random_state = np.random.RandomState()
        return func(random_state, *args, **kwargs)
    return wrapper

@random_state_decorator
def example_function(random_state, graph):
    # Example usage of the random state in a function
    for node in graph.nodes():
        graph.nodes[node]['random_value'] = random_state.rand()
    return graph

# Example usage
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
G = example_function(G)
print(G.nodes(data=True))
