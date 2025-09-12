
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(['Alice', 'Bob', 'Charlie'])
G.add_edges_from([('Alice', 'Bob'), ('Alice', 'Charlie')])

# Get the adjacency matrix for the graph
adj_matrix = nx.adjacency_matrix(G)

# Create a mixing matrix from the adjacency matrix
mixing_matrix = np.dot(np.linalg.inv(adj_matrix), np.eye(len(G)))
