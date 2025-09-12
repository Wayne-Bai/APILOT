import networkx as nx
from scipy.sparse import csr_matrix

# Create a graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)

# Get the number of nodes
num_nodes = G.number_of_nodes()

# Create an empty adjacency matrix
adj_matrix = csr_matrix((num_nodes, num_nodes), dtype=int)

# Fill the adjacency matrix with edges
for edge in G.edges():
    start_node, end_node = edge
    adj_matrix[start_node, end_node] = 1
    adj_matrix[end_node, start_node] = 1

print(adj_matrix)
