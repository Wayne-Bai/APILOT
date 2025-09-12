import networkx as nx

# Create an empty undirected graph
G = nx.Graph()

# Add nodes
G.add_node('A')
G.add_node('B')
G.add_node('C')

# Add edges
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('A', 'C')

# Print the graph
print(G.nodes())
print(G.edges())
