import networkx as nx
import pickle

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_node("Node1")
G.add_node("Node2")
G.add_node("Node3")

# Add edges
G.add_edge("Node1", "Node2")
G.add_edge("Node2", "Node3")

# Write the graph to a pickle file
with open("graph.pkl", "wb") as f:
    pickle.dump(G, f)
