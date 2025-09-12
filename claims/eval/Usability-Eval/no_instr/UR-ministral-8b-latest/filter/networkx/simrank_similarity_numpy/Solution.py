import networkx as nx
import numpy as np

# Initialize an example graph
G = nx.Graph()
edges = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 4)]
G.add_edges_from(edges)

# Calculate PageRank
page_rank = nx.pagerank(G)

# Convert PageRank dictionary to numpy array
page_rank_np = np.array(list(page_rank.values()))

# Calculate SimRank
simrank = np.dot(page_rank_np, np.transpose(page_rank_np))

print("PageRank of nodes:", page_rank)
print("SimRank matrix:", simrank)
