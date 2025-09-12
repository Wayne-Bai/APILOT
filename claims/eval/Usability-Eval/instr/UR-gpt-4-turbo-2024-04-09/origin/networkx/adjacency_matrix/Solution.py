import networkx as nx

def get_adjacency_matrix(G):
    # Convert the graph to an adjacency matrix
    return nx.adjacency_matrix(G)

# Example usage:
# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4)])

# Get the adjacency matrix
adj_matrix = get_adjacency_matrix(G)
print(adj_matrix.todense())
