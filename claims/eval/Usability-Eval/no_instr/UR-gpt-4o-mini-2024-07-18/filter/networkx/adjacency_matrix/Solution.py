import networkx as nx

def get_adjacency_matrix(G):
    return nx.adjacency_matrix(G).todense()

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (1, 3)])
adj_matrix = get_adjacency_matrix(G)
print(adj_matrix)
