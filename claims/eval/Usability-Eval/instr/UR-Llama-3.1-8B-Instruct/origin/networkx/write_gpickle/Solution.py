import networkx as nx
import pickle

# Create an empty graph
G = nx.Graph()

# Add some nodes and edges
G.add_node("Node1")
G.add_node("Node2")
G.add_node("Node3")
G.add_edge("Node1", "Node2")
G.add_edge("Node2", "Node3")
G.add_edge("Node1", "Node3")

# Write the graph to a file using pickle
with open('graph.pkl', 'wb') as handle:
    pickle.dump(G, handle)

# Read the graph from the file using pickle
with open('graph.pkl', 'rb') as handle:
    loaded_G = pickle.load(handle)

# Print the nodes and edges of the loaded graph
print("Nodes:", loaded_G.nodes())
print("Edges:", loaded_G.edges())
