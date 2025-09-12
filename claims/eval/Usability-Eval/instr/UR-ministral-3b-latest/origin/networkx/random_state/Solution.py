import networkx as nx
import numpy as np

class RandomStateDecorator(object):
    def __init__(self, rng):
        self.rng = rng

    def __getattr__(self, name):
        if hasattr(self.rng, name):
            return getattr(self.rng, name)
        raise AttributeError("'RandomStateDecorator' object has no attribute '%s'" % name)

default_random_state = RandomStateDecorator(np.random.RandomState())

