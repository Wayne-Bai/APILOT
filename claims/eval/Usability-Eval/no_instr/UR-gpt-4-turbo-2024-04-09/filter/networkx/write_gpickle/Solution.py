import networkx as nx
import pickle

# Create a graph
G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')

# Write graph to a pickle file
with open('graph.pkl', 'wb') as f:
    pickle.dump(G, f)
