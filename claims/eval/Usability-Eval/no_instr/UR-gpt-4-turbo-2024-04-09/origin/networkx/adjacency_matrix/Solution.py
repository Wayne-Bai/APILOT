import networkx as nx

def adjacency_matrix(G):
    return nx.adjacency_matrix(G)

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3)])

matrix = adjacency_matrix(G)
print(matrix.todense())
