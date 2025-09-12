
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
G.add_nodes_from(['A', 'B', 'C'])

# Add edges to the graph
G.add_edges_from([('A', 'B'), ('A', 'C')])

# Get the adjacency matrix of the graph
adj_matrix = nx.to_numpy_matrix(G)

print(adj_matrix)
