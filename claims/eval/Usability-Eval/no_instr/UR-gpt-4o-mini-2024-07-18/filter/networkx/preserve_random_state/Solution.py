import networkx as nx
import numpy as np
import functools

def preserve_random_state(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get the current random state
        state = np.random.get_state()
        try:
            return func(*args, **kwargs)
        finally:
            # Restore the random state
            np.random.set_state(state)
    return wrapper

# Example usage
@preserve_random_state
def example_function():
    # This function will not alter the numpy random state
    print("Random number:", np.random.rand())

# Call the example function
example_function()
