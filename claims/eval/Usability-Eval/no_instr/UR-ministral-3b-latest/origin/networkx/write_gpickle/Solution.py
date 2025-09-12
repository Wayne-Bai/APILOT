import networkx as nx
import pickle

# Create a graph
G = nx.Graph()

# Add nodes (there are no attributes here)
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

# Serialize the graph to a pickle file
with open('graph.pkl', 'wb') as f:
    pickle.dump(G, f)

