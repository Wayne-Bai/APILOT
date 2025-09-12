import networkx as nx
import numpy as np

class RandomStateDecorator:
    def __init__(self, random_state):
        self.random_state = np.random.RandomState(random_state)

    def __getattr__(self, name):
        return getattr(self.random_state, name)

# Usage
random_state = RandomStateDecorator(0)
print(random_state.rand(2))
