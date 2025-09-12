import networkx as nx

# Define the graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_node('A')
G.add_node('B')
G.add_edge('A', 'B')

# Compute the average degree connectivity
avg_degree_connectivity = nx.average_degree_connectivity(G)
print("The average degree connectivity of the graph is:", avg_degree_connectivity)
