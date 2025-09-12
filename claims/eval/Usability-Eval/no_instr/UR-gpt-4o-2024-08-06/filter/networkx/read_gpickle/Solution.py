import networkx as nx
import pickle

# Load the graph from a pickle file
with open('graph.pkl', 'rb') as file:
    graph = pickle.load(file)

# Checking if the graph is loaded
print("Graph loaded from pickle:")
print("Nodes:", graph.nodes())
print("Edges:", graph.edges())
