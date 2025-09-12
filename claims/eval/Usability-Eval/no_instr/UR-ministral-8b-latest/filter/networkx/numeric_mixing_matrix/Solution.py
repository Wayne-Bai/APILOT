import networkx as nx
import numpy as np

def create_mixing_matrix(G):
    # Find the largest eigenvalue of the adjacency matrix
    adjacency_matrix = nx.adjacency_matrix(G).todense()
    largest_eigenvalue, _ = np.linalg.eig(adjacency_matrix)[0].real

    # Create the mixing matrix
    mixing_matrix = np.ones((G.number_of_nodes(), G.number_of_nodes()))
    for i in range(G.number_of_nodes()):
        for j in range(G.number_of_nodes()):
            if i != j:
                mixing_matrix[i][j] = largest_eigenvalue / G.size(G.nodes[i])

    return mixing_matrix

# Example usage
if __name__ == "__main__":
    # Create a simple graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4)])

    # Generate mixing matrix
    mixing_matrix = create_mixing_matrix(G)
    print('Mixing Matrix:')
    print(mixing_matrix)
