import networkx as nx
import pickle

# Create a simple graph
G = nx.Graph()

# Add nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Add edges
G.add_edge(1, 2)
G.add_edge(2, 3)

# Serialize the graph using pickle
with open('graph.pkl', 'wb') as file:
    pickle.dump(G, file)
