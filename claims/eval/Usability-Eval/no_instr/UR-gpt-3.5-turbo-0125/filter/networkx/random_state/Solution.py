
import networkx as nx
import numpy as np

def random_state_decorator(func):
    def wrapper(*args, **kwargs):
        random_state = np.random.RandomState()
        return func(random_state, *args, **kwargs)
    return wrapper
