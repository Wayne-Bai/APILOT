import networkx as nx
import pickle

# Load the graph object from a pickle file
with open('graph.pkl', 'wb') as f:
    graph = pickle.load(f)

print(graph)
