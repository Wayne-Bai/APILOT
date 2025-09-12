import networkx as nx

def calculate_google_matrix(graph):
    # Create a copy of the original graph to avoid modifying the original graph
    graph_copy = graph.copy()

    # Add edge weights (page ranks in this case)
    for edge in graph_copy.edges():
        graph_copy[edge[0]][edge[1]]['weight'] = 1.0 / graph_copy.out_degree(edge[0])

    # Initialize the Google matrix as an identity matrix
    google_matrix = nx.to_numpy_matrix(graph_copy, dtype=float)

    # Transpose the Google matrix and return
    return google_matrix.transpose()

# Create a directed graph
graph = nx.DiGraph()
graph.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4)])

# Calculate the Google matrix
google_matrix = calculate_google_matrix(graph)
print(google_matrix)
