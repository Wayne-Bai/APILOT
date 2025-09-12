
import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C'])
G.add_edges_from([('A', 'B'), ('A', 'C')])

# Compute the numeric mixing matrix for the graph
num_mixing_matrix = nx.numerical.mixing_matrix(G, degree=True)

print(num_mixing_matrix)
