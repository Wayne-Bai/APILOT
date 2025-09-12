
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(['A', 'B', 'C', 'D'])

# Add edges to the graph
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')])

# Get the adjacency matrix of the graph
adj_matrix = nx.to_numpy_matrix(G)

print(adj_matrix)
