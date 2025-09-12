import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# Print short summary of information for the graph G
print("Graph G:")
print("Number of nodes: ", G.number_of_nodes())
print("Number of edges: ", G.number_of_edges())

# Print short summary of information for a node n
node_n = 2
print("\nInformation for node", node_n, ":")
print("Neighbors: ", list(G.neighbors(node_n)))
