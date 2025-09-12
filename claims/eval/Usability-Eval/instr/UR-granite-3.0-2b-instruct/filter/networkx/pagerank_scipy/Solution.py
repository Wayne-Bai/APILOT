import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')

# Add edges with weights (incoming links)
G.add_edge('A', 'B', weight=0.5)
G.add_edge('A', 'C', weight=0.3)
G.add_edge('B', 'C', weight=0.2)
G.add_edge('B', 'D', weight=0.4)
G.add_edge('C', 'D', weight=0.1)

# Calculate PageRank
pagerank = nx.pagerank(G)

# Print PageRank of each node
for node, pr in pagerank.items():
    print(f"Node: {node}, PageRank: {pr}")
