# Step 1: Import the networkx module
import networkx as nx

# Create a graph
G = nx.Graph()

# Step 3: Return the adjacency matrix as a NumPy recarray
adjacency_matrix = nx.to_numpy_recarray(G)
print(adjacency_matrix)
