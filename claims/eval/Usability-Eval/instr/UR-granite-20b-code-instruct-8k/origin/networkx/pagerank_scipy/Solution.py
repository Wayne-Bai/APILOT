import networkx as nx

# Define your graph
G = nx.Graph()

# Add edges to your graph
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# Calculate the PageRank
page_rank = nx.pagerank(G)

# Print the PageRank
print(page_rank)
