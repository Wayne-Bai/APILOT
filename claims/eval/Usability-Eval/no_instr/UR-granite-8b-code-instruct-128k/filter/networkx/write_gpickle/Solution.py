
import networkx as nx

G = nx.Graph()

# Add nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Add edges
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)

# Write graph in Python pickle format
import pickle
with open('graph.pkl', 'wb') as f:
    pickle.dump(G, f)
