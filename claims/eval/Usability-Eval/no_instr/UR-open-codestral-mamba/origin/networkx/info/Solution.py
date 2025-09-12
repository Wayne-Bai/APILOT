import networkx as nx

# Creating a graph
G = nx.Graph()

# Adding nodes
G.add_node("Node1")
G.add_node("Node2")
G.add_node("Node3")

# Adding edges
G.add_edge("Node1", "Node2")
G.add_edge("Node1", "Node3")
G.add_edge("Node2", "Node3")

# Printing the summary
print("Nodes: ", G.nodes())  # Printing the nodes
print("Edges: ", G.edges())  # Printing the edges

# Summary of information for a node
node_info = G.nodes["Node1"]
print(f"Node 'Node1' Info: {node_info}")

# Summary of information for a edge
edge_info = G.edges["Node1", "Node2"]
print(f"Edge ('Node1', 'Node2') Info: {edge_info}")
