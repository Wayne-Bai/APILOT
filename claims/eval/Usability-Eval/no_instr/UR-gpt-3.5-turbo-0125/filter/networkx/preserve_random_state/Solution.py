
import networkx as nx
import numpy as np

def preserve_random_state(func):
    def wrapper(*args, **kwargs):
        state = np.random.get_state()
        result = func(*args, **kwargs)
        np.random.set_state(state)
        return result
    return wrapper

@preserve_random_state
def your_function():
    # Your function code here
    pass
