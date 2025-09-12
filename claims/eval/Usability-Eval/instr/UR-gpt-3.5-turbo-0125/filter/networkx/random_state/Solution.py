
import networkx as nx
import numpy as np

def random_state_decorator(func):
    def wrapper(*args, **kwargs):
        rs = np.random.RandomState()
        return func(rs, *args, **kwargs)
    return wrapper
