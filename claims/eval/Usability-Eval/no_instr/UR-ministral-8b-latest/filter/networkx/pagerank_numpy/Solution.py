import networkx as nx

# Create a graph
G = nx.DiGraph()

# Add edges
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')
G.add_edge('C', 'D')
G.add_edge('D', 'C')

# Compute PageRank
pagerank = nx.pagerank(G)

# Print PageRank of each node
for node in pagerank:
    print(f"Node {node}: {pagerank[node]}")
