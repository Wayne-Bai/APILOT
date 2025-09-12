
import networkx as nx
import pickle

# Create a graph
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_edge(1, 2)

# Write graph in Python pickle format
with open("graph.pickle", "wb") as f:
    pickle.dump(G, f)
