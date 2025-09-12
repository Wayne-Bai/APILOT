import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(5, 1)

# Calculate the HITS hub matrix
hits_hub_matrix = nx.hits_hub(G)

# Print the HITS hub matrix
print(hits_hub_matrix)
