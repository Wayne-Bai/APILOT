import networkx as nx
import numpy as np

class RandomStatePreserver:
    def __init__(self):
        self.state = np.random.get_state()

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            np.random.set_state(self.state)
            return func(*args, **kwargs)
        return wrapper

@RandomStatePreserver()
def some_function(seed):
    np.random.seed(seed)
    # Your function code here
    pass

# Usage
some_function(0)
