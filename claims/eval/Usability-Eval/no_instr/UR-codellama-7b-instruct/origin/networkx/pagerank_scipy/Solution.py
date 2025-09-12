
import networkx as nx

# Create a simple graph with three nodes
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C'])
G.add_edges_from([('A', 'B'), ('A', 'C')])

# Calculate the PageRank of the nodes in the graph
pageranks = nx.pagerank(G)
print(pageranks)
