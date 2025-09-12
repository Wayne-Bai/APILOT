import networkx as nx
import numpy as np
from functools import wraps

def preserve_random_state(func):
    """Decorator to preserve the numpy.random state during a function call."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Save the current random state
        state = np.random.get_state()
        try:
            # Call the decorated function
            return func(*args, **kwargs)
        finally:
            # Restore the random state
            np.random.set_state(state)
    return wrapper

# Example usage
@preserve_random_state
def example_function():
    print("Random number:", np.random.rand())
    # Random number generation that will not affect the global state
    random_numbers = np.random.rand(5)
    print("Generated random numbers:", random_numbers)

# Test the decorator
example_function()
print("Random number after function call:", np.random.rand())
