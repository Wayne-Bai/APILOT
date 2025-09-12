import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'A')])

# Calculate PageRank
pr = nx.pagerank(G, alpha=0.85, personalization=None, max_iter=100, tol=1.0e-6, n_iter=None, weight='weight', dangling=None)

# Print the PageRank of each node
for node, rank in pr.items():
    print(f"Node {node}: {rank}")
