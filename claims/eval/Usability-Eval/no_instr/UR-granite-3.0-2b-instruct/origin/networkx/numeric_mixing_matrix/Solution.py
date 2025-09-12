import networkx as nx

def generate_mixing_matrix(graph):
    # Calculate the adjacency matrix
    adj_matrix = nx.adjacency_matrix(graph)

    # Calculate the degree matrix
    degree_matrix = nx.degree_matrix(graph)

    # Calculate the Laplacian matrix
    laplacian_matrix = adj_matrix - degree_matrix

    # Calculate the eigenvectors and eigenvalues of the Laplacian matrix
    eigenvalues, eigenvectors = np.linalg.eig(laplacian_matrix.toarray())

    # Sort the eigenvalues and eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    # Calculate the numeric mixing matrix
    mixing_matrix = sorted_eigenvectors.T

    return mixing_matrix
