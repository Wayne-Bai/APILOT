import numpy as np
import networkx as nx

class Decorator(nx.Graph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __call__(self, *args, **kwargs):
        return np.random.RandomState()

G = Decorator()
