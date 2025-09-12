import networkx as nx
import numpy as np

def calculate_simrank(G, max_iter=100, tol=1.0e-8):
    """
    Compute SimRank similarity between nodes in graph G.

    Parameters:
    G (nx.Graph): The input graph.
    max_iter (int, optional): Maximum number of iterations. Defaults to 100.
    tol (float, optional): Convergence tolerance. Defaults to 1e-8.

    Returns:
    sim_dict (dict): Dictionary containing the SimRank similarity between each pair of nodes.
    """

    # Get the adjacency matrix of the graph
    A = nx.to_numpy_array(G)

    # Initialize the similarity matrix with ones on the diagonal
    S = np.ones_like(A)

    for _ in range(max_iter):
        # Compute the new similarity matrix using SimRank formula
        S_new = (np.dot(np.dot(A, S), A.T) * 2) / (np.dot(np.dot(A, S), A.T) + S + np.eye(A.shape[0]))

        # Check for convergence
        if np.all(np.abs(S_new - S) < tol):
            break

        S = S_new

    # Convert the similarity matrix to a dictionary
    sim_dict = {}
    for i in range(A.shape[0]):
        for j in range(i+1):
            sim_dict[(i, j)] = S[i, j]
            sim_dict[(j, i)] = S[i, j]  # Ensure symmetry

    return sim_dict

# Example usage
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])

    # Calculate SimRank similarity
    sim_dict = calculate_simrank(G)

    # Print the results
    for (u, v), sim in sorted(sim_dict.items()):
        print(f"SimRank({u}, {v}) = {sim:.4f}")
