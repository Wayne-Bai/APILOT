import networkx as nx
import numpy as np

# Create an empty graph
G = nx.Graph()

# Add nodes
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')

# Add edges
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')
G.add_edge('D', 'A')

# Return the graph adjacency matrix as a NumPy recarray
adj_matrix = nx.to_numpy_array(G)
numpy_recarray = np.lib.recfunction.convert_to_recarray(adj_matrix, dtype=[('A', 'd'), ('B', 'd'), ('C', 'd'), ('D', 'd')])

print(numpy_recarray)
