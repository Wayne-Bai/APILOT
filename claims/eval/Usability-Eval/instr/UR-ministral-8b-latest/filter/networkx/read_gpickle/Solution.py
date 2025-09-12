import networkx as nx
import pickle

# Load graph from pickle file
with open('graph.pkl', 'rb') as f:
    G = pickle.load(f)

# Print some information about the loaded graph
print(f"Number of nodes: {G.nodes}")
print(f"Number of edges: {G.edges}")
