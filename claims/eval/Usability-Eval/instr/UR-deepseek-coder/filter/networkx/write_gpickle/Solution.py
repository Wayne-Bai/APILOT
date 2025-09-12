import networkx as nx
import pickle

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Serialize the graph to a pickle file
with open('graph.pkl', 'wb') as f:
    pickle.dump(G, f)
