import networkx as nx

# Create a new graph
G = nx.Graph()

# Add nodes with unique labels
G.add_node("Node1")
G.add_node("Node2")
G.add_node("Node3")

# Print the nodes and their labels
for node in G.nodes:
    print(f"Node: {node}, Label: {G.nodes[node]['label']}")
