import networkx as nx
from networkx.algorithms.community import label_propagation_communities

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(["Node1", "Node2", "Node3", "Node4", "Node5"])

# Add edges
G.add_edge("Node1", "Node2")
G.add_edge("Node2", "Node3")
G.add_edge("Node3", "Node4")
G.add_edge("Node4", "Node5")
G.add_edge("Node5", "Node1")

# Use label propagation to find communities
communities = label_propagation_communities(G)

# Print the communities
for i, c in enumerate(communities):
    print(f"Community {i+1}: {c}")
