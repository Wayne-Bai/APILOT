import networkx as nx

# Creating a directed graph
G = nx.DiGraph()

# Adding edges to the graph
# Add your edges here in the format (node1, node2)
# For example:
# G.add_edges_from([(1,2),(2,3),(3,1)])

# Compute PageRank
pagerank = nx.pagerank(G)

# Printing the PageRank of the nodes
for node, rank in pagerank.items():
    print(f"Node: {node}  PageRank: {rank}")
