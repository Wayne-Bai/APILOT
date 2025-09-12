
import networkx as nx

# create a sample graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 3)

# compute the PageRank of the nodes in the graph
pagerank = nx.pagerank(G)

print("PageRank of node 1:", pagerank[1])
print("PageRank of node 2:", pagerank[2])
print("PageRank of node 3:", pagerank[3])
