import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_node('A')
G.add_node('B')
G.add_node('C')

# Add edges
G.add_edge('A', 'B')
G.add_edge('B', 'C')

# Print the graph
print(G.edges())
