import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_edge("A", "B")
G.add_edge("B", "C")

# Calculate PageRank
pr = nx.pagerank(G)

# Print the PageRank of each node
for node, pr_value in pr.items():
    print(f"Node {node}: {pr_value}")
