import networkx as nx
import numpy as np

# Decorator to preserve the numpy.random state
def preserve_random_state(func):
    def wrapper(*args, **kwargs):
        np.random_state = np.random.get_state()
        try:
            return func(*args, **kwargs)
        finally:
            np.random.set_state(np.random_state)
    return wrapper
