import networkx as nx
import numpy as np
import functools

def preserve_random_state(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Save the current random generator state
        state = np.random.get_state()
        
        try:
            # Call the decorated function
            result = func(*args, **kwargs)
        finally:
            # Restore the random generator state
            np.random.set_state(state)
        
        return result
    return wrapper

@preserve_random_state
def example_function():
    print("Random number:", np.random.rand())

# Example usage of the decorator
example_function()
