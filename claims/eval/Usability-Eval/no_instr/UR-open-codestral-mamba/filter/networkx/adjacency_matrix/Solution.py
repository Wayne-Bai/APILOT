
import networkx as nx

def adjacency_matrix(G):
    return nx.to_numpy_matrix(G)

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])
print(adjacency_matrix(G))
