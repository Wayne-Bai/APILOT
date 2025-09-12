import networkx as nx

# Define a function to compute the spectral ordering of a graph
def spectral_ordering(G):
    # Compute the eigenvectors and eigenvalues of the graph matrix
    eigs, vecs = nx.linalg.eigens(G)

    # Extract the Fiedler vector from the eigenvectors and eigenvalues
    fiedler_vec = vecs[:, 1]

    # Sort the nodes of the graph based on their corresponding elements in the Fiedler vector
    sorted_nodes = sorted(G.nodes(), key=lambda n: fiedler_vec[n])

    return sorted_nodes

# Create a small example graph
G = nx.complete_graph(5)

# Compute the spectral ordering of the graph
ordered_nodes = spectral_ordering(G)

print("Spectral ordering:", ordered_nodes)
