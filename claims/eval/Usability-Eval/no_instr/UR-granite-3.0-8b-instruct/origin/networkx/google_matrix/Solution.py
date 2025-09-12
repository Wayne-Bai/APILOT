import networkx as nx

def calculate_google_matrix(graph):
    n = len(graph.nodes())
    G = nx.from_numpy_array(nx.laplacian_matrix(graph).toarray())
    G = G / G.sum(axis=1, keepdims=True)
    return G

# Example usage:
# Create a graph
graph = nx.Graph()
graph.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

# Calculate the Google matrix
google_matrix = calculate_google_matrix(graph)
print(google_matrix)
