import networkx as nx
import pickle

# Load the graph object from a pickle file
with open('graph.pkl', 'rb') as f:
    graph = pickle.load(f)

# Now 'graph' is a NetworkX graph object that was serialized and saved in pickle format
