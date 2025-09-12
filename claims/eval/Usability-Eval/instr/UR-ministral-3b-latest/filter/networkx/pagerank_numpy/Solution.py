import networkx as nx

# Create graph G
G = nx.Graph()

# Add nodes to graph G
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges to graph G
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(3, 5)

# Assign PageRank to each node in graph G
pr = nx.pagerank(G)

# Print PageRank of each node
print("PageRank of each node in the graph:")
for node, rank in pr.items():
    print(f"Node: {node}, PageRank: {rank}")

