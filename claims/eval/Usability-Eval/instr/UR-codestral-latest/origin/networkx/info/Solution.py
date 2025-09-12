import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from(['A', 'B', 'C', 'D'])
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])

# Print graph summary
print("Number of nodes: ", G.number_of_nodes())
print("Number of edges: ", G.number_of_edges())

# Print node 'A' summary
node = 'A'
print(f"Node: {node}")
print("Degree: ", G.degree(node))
print("Neighbors: ", list(G.neighbors(node)))
