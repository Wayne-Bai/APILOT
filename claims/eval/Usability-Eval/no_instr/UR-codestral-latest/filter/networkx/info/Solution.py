import networkx as nx

# Create a graph
G = nx.Graph()

# Adding nodes and edges
G.add_nodes_from(["A", "B", "C", "D"])
G.add_edges_from([("A", "B"), ("B", "C"), ("C", "D")])

# Printing summary for the graph G
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Nodes:", G.nodes())
print("Edges:", G.edges())

# To print summary for a node 'A' (replace 'A' with desired node)
degree = G.degree("A")
print("\nNode A has degree:", degree)
neighbors = list(G.neighbors("A"))
print("Node A's neighbors are:", neighbors)
