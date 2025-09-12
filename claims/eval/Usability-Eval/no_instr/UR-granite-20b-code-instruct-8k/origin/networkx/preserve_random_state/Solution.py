
import networkx as nx
import numpy as np

def preserve_numpy_random_state(func):
    def wrapper(*args, **kwargs):
        state = np.random.get_state()
        np.random.set_state(state)
        result = func(*args, **kwargs)
        np.random.set_state(state)
        return result
    return wrapper
