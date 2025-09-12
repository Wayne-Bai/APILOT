import networkx as nx

# create a sample graph with 4 nodes and edges
G = nx.Graph()
G.add_edges_from([(0,1),(1,2),(2,3)])

# compute the PageRank of each node
page_rank = nx.pagerank(G)

# print the PageRank of each node
print("PageRank of nodes:")
for i in range(len(G)):
    print("Node", i, ":", page_rank[i])
