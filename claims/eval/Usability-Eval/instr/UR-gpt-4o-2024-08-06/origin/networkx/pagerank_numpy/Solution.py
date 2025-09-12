import networkx as nx

# Create a directed graph object
G = nx.DiGraph()

# Add nodes and edges to the graph
# For example:
G.add_edges_from([
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 1),
    (3, 4),
    (4, 2),
])

# Compute PageRank
# You can adjust the alpha parameter which is the damping factor (0.85 is a common choice)
page_rank = nx.pagerank(G, alpha=0.85)

# Output the PageRank of each node
print(page_rank)
