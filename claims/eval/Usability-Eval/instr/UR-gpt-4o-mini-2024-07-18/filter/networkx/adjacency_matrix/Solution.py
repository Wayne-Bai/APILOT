import networkx as nx

def adjacency_matrix_of_graph(G):
    return nx.to_numpy_array(G)

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4)])
adjacency_matrix = adjacency_matrix_of_graph(G)
print(adjacency_matrix)
