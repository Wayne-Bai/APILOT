import networkx as nx
import numpy as np
from functools import wraps

def preserve_random_state(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Save the current state of numpy's random number generator
        state = np.random.get_state()
        try:
            # Execute the function
            result = func(*args, **kwargs)
        finally:
            # Restore the state of numpy's random number generator
            np.random.set_state(state)
        return result
    return wrapper

# Example usage
@preserve_random_state
def random_operations():
    print(np.random.rand(3))  # Random operation

# Test the decorator
random_operations()  # This will print random numbers but won't affect the RNG state outside
