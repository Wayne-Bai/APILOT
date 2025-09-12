import networkx as nx

def generate_mixing_matrix(graph):
    # Ensure the graph is undirected
    graph = nx.to_undirected(graph)

    # Calculate the number of nodes
    num_nodes = graph.number_of_nodes()

    # Initialize the mixing matrix with zeros
    mixing_matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    # Fill the mixing matrix with the adjacency matrix
    for node in range(num_nodes):
        for neighbor in graph.neighbors(node):
            mixing_matrix[node][neighbor] = 1

    return mixing_matrix
