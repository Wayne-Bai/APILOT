import networkx as nx

# Generate a graph
G = nx.Graph()

# Add nodes to the graph
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)

# Compute the PageRank of the nodes in the graph
page_rank = nx.pagerank(G)

# Print the PageRank of each node
for node, rank in page_rank.items():
    print(f"PageRank of node {node}: {rank}")
