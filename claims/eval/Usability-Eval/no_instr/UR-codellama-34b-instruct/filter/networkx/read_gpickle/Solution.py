import pickle
from networkx import Graph

# Read the graph from a pickle file
with open("graph.pickle", "rb") as f:
    graph = pickle.load(f)

# Convert the graph to a NetworkX Graph object
G = Graph(graph)
