import networkx as nx

# Assuming G is your graph and n is the node you want to inspect
G = nx.Graph()  # replace with your graph
n = 'node_name'  # replace with the node you want to inspect

# Print summary of the graph G
print("Summary of Graph G:")
print("Number of nodes: ", G.number_of_nodes())
print("Number of edges: ", G.number_of_edges())

# Print summary of the node n
print("\nSummary of Node", n)
print("Degree: ", G.degree(n))
print("Neighbors: ", G.neighbors(n))
