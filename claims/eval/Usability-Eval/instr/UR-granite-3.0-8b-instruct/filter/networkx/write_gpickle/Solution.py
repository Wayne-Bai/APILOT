import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes
G.add_node("Node1")
G.add_node("Node2")

# Add edges
G.add_edge("Node1", "Node2")

# Write graph to pickle file
with open("graph.pickle", "wb") as f:
    pickle.dump(G, f)
