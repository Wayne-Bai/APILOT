import networkx as nx

# Define the graph and attributes
G = nx.Graph()
G.add_node("A", weight=1)
G.add_node("B", weight=2)
G.add_edge("A", "B", weight=3)

# Calculate the numeric mixing matrix for the attribute 'weight'
M = nx.numeric_mixing_matrix(G, attribute="weight")
print(M)
