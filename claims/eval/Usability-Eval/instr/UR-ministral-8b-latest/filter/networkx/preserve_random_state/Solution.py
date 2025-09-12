import numpy as np
import networkx as nx

class NumpyRandomStatePreserver:
    def __init__(self):
        self.original_state = None

    def __enter__(self):
        self.original_state = np.random.get_state()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        np.random.set_state(self.original_state)

# Usage example with NetworkX
# G = nx.Graph()
# with NumpyRandomStatePreserver():
#     for _ in range(10):
#         G.add_node(np.random.randint(0, 100))
#         G.add_edge(np.random.randint(0, 100), np.random.randint(0, 100))
# print(list(G.nodes))
