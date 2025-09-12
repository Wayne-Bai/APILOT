import networkx as nx
import pickle

# Create a graph object, e.g., a simple undirected graph
G = nx.Graph()

# Add some nodes and edges to the graph
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

# Specify the filename for the pickle file
filename = 'graph.pickle'

# Write the graph to a Python pickle file
with open(filename, 'wb') as f:
    pickle.dump(G, f)
