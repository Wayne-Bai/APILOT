import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_node('A')
G.add_node('B')
G.add_edge('A', 'B')

# Print summary information about the graph
print(nx.info(G))
