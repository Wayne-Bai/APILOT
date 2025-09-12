import networkx as nx

# Create a sample graph
G = nx.gnp_random_graph(10, 0.5)

# Calculate PageRank for each node
page_rank = nx.pagerank(G, alpha=0.85)

# Print the results
for node in G.nodes():
    print(f"{node}: {page_rank[node]}")
