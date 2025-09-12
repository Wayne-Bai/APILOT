import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges
# Example edges (you can add any graph structure you desire)
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A'), ('D', 'C')]
G.add_edges_from(edges)

# Compute PageRank
page_rank = nx.pagerank(G)

# Print PageRank of each node
for node, rank in page_rank.items():
    print(f"Node: {node}, PageRank: {rank}")
