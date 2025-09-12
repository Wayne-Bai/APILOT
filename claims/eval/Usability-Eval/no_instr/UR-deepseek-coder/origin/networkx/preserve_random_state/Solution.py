import networkx as nx
import numpy as np

def preserve_random_state(func):
    def wrapper(*args, **kwargs):
        # Save the current state of numpy.random
        current_state = np.random.get_state()
        try:
            # Execute the function
            result = func(*args, **kwargs)
        finally:
            # Restore the original state of numpy.random
            np.random.set_state(current_state)
        return result
    return wrapper

# Example usage
@preserve_random_state
def create_random_graph(n, p):
    G = nx.erdos_renyi_graph(n, p)
    return G

# Test the decorator
graph = create_random_graph(10, 0.5)
print(graph.nodes)
