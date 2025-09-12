import networkx as nx
import pickle

# Create a sample graph
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'C', weight=2)

# Write to a pickle file
with open('graph.pkl', 'wb') as f:
    pickle.dump(G, f)
