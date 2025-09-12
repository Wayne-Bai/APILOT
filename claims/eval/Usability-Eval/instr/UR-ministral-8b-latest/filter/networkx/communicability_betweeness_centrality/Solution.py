import networkx as nx

# Function to calculate communicability for all pairs of nodes
def calculate_communicability(G):
    # Create an adjacency matrix
    adj_matrix = nx.adj_matrix(G).toarray()

    # Initialize to_array variable
    communicability_matrix = None

    # Use dynamic programming to fill in the communicability matrix
    n = len(G.nodes)
    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    if adj_matrix[j][i] == 1:
                        communicability_matrix[i][j] = sum([adj_matrix[k][i] * adj_matrix[k][j] for k in range(n)]) * 0.5 ** (1 - sum(adj_matrix[i][:][j]))

    return communicability_matrix

# Example usage
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3)], weight=1)
communicability_matrix = calculate_communicability(G)
print(communicability_matrix)
