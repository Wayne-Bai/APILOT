
import networkx as nx

# create a sample graph
G = nx.gnp_random_graph(10, 0.5)

# compute the PageRank of each node
page_rank = nx.pagerank(G)

# print the PageRank of each node
for node in G:
    print("Node", node, "has PageRank", page_rank[node])
