import networkx as nx

# Create a graph
G = nx.DiGraph()

# Add nodes
G.add_node('Node 1')
G.add_node('Node 2')
G.add_node('Node 3')

# Add edges
G.add_edge('Node 1', 'Node 2')
G.add_edge('Node 2', 'Node 3')
G.add_edge('Node 3', 'Node 1')

# Calculate PageRank
pagerank = nx.pagerank(G)
print(pagerank)
