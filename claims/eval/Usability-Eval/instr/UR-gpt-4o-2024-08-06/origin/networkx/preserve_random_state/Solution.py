import networkx as nx
import numpy as np

def preserve_random_state(func):
    """
    A decorator to preserve the numpy.random state during the execution of a function.
    
    Args:
    - func: The function to wrap.
    
    Returns:
    - The wrapped function that restores numpy.random state after its execution.
    """
    def wrapper(*args, **kwargs):
        # Save the current state of the numpy random generator
        state = np.random.get_state()
        try:
            # Execute the wrapped function
            result = func(*args, **kwargs)
        finally:
            # Restore the saved state of the numpy random generator
            np.random.set_state(state)
        return result

    return wrapper

# Example Usage
@preserve_random_state
def random_graph_example():
    # Some function that uses numpy.random internally
    G = nx.erdos_renyi_graph(10, 0.5)  # Generates a random graph
    print(np.random.rand())  # Some random operation

# Call the function
random_graph_example()
