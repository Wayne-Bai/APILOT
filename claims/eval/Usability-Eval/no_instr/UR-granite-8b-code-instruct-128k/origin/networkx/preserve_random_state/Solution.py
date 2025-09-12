import networkx as nx
import numpy as np
from functools import wraps

def preserve_random_state(func):
    """Decorator to preserve the numpy.random state during a function."""
    @wraps(func)
    def wrapped(*args, **kwargs):
        state = np.random.get_state()
        try:
            return func(*args, **kwargs)
        finally:
            np.random.set_state(state)
    return wrapped
