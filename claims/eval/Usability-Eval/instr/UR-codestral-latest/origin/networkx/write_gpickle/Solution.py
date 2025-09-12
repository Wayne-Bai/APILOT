import pickle
import networkx as nx

# Creating a graph
G = nx.Graph()

# Adding nodes
G.add_nodes_from([1, 2, 3, 4])

# Adding edges
G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 4)])

# Pickling the graph
with open('graph.pkl', 'wb') as f:
    pickle.dump(G, f)
