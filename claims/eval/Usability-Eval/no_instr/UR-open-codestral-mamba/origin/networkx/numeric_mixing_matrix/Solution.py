import networkx as nx
import numpy as np
import pandas as pd

def get_numeric_mixing_matrix(graph, attribute):
    mixing_matrix = nx.attr_matrix(graph, node_attr=attribute, normalized=True)
    return pd.DataFrame(mixing_matrix[0], index=mixing_matrix[1], columns=mixing_matrix[1])

# Create a sample graph to test our function on
G = nx.Graph()
G.add_node("A", attribute=1)
G.add_node("B", attribute=2)
G.add_node("C", attribute=3)
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("A", "C")

print(get_numeric_mixing_matrix(G, 'attribute'))
