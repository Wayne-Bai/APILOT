import networkx as nx
import pickle

# Create a sample graph
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'C', weight=3)
G.add_edge('C', 'A', weight=5)

# Write the graph to a pickle file
with open('graph.pkl', 'wb') as f:
    pickle.dump(G, f)

# To read the graph back from the pickle file
with open('graph.pkl', 'rb') as f:
    loaded_graph = pickle.load(f)

# Optional: Verify that the loaded graph matches the original
assert nx.is_isomorphic(G, loaded_graph)
