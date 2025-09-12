import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2, weight=0.5)
G.add_edge(1, 3, weight=0.3)
G.add_edge(2, 3, weight=0.7)

# Generate the numeric mixing matrix for attribute
numeric_mixing_matrix = nx.numeric_mixing_matrix(G, attribute='weight')

# Print the numeric mixing matrix
print(numeric_mixing_matrix)
