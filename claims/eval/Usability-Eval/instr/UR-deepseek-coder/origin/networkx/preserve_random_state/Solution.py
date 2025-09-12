import networkx as nx
import numpy as np

def preserve_random_state(func):
    def wrapper(*args, **kwargs):
        # Save the current state of numpy.random
        current_state = np.random.get_state()
        try:
            # Call the original function
            result = func(*args, **kwargs)
        finally:
            # Restore the original state of numpy.random
            np.random.set_state(current_state)
        return result
    return wrapper

# Example usage with a NetworkX function
@preserve_random_state
def example_function(G):
    # Example NetworkX function that might use random numbers
    nx.draw(G, with_labels=True)

# Create a sample graph
G = nx.erdos_renyi_graph(10, 0.5)

# Call the example function
example_function(G)
