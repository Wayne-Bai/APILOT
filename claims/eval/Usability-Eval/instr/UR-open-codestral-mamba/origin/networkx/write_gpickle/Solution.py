import pickle
import networkx as nx

# Create a new graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 3)

# Save the graph to a file in a pickle format
with open('graph.pickle', 'wb') as f:
    pickle.dump(G, f)
