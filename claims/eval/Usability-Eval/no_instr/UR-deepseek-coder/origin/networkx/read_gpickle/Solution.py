import networkx as nx
import pickle

# Load the graph from a pickle file
with open('graph.pkl', 'rb') as f:
    G = pickle.load(f)

# Now G is a NetworkX graph object that was saved in pickle format
