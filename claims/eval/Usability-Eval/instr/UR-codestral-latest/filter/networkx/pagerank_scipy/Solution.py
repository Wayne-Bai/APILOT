import networkx as nx

# Create a DiGraph object
G = nx.DiGraph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)
G.add_edge(5, 1)
G.add_edge(5, 3)
G.add_edge(5, 4)

# Compute the PageRank
pagerank = nx.pagerank(G)

print("PageRank of the nodes in the graph:", pagerank)
