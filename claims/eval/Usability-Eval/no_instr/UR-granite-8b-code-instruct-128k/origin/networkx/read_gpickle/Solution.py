import pickle
import networkx as nx

# Load the pickle file
with open('graph.pickle', 'rb') as f:
    graph = pickle.load(f)

# Print the graph object
print(graph)
