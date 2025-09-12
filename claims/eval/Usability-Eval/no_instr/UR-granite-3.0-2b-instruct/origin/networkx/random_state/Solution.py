import networkx as nx
import numpy as np

class RandomStateDecorator:
    def __init__(self, graph):
        self.graph = graph
        self.random_state = np.random.RandomState()

    def generate_random_state(self):
        return self.random_state

    def set_random_state(self, rs):
        self.random_state = rs

# Example usage:
G = nx.Graph()
rs_decorator = RandomStateDecorator(G)
rs = rs_decorator.generate_random_state()
rs_decorator.set_random_state(rs)
