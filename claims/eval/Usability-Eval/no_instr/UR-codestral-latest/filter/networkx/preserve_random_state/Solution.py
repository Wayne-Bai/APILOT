import numpy as np
import networkx as nx
from functools import wraps

def preserve_numpy_random_state(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        state = np.random.get_state()
        try:
            return func(*args, **kwargs)
        finally:
            np.random.set_state(state)
    return wrapper
