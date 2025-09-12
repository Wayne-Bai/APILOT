import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'A')])

# Compute the PageRank
page_rank_values = nx.pagerank(G)

print(page_rank_values)
