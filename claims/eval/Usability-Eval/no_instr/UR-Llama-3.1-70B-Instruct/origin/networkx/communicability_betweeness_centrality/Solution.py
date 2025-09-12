import networkx as nx
import numpy as np

def communicability(G):
    """
    Compute the communicability between all pairs of nodes in G.
    
    Parameters
    ----------
    G : networkx.Graph
        The input graph.
        
    Returns
    -------
    comm : numpy.ndarray
        A matrix of communicability between all pairs of nodes in G.
    """
    
    # Get the adjacency matrix of the graph
    A = nx.to_numpy_array(G, dtype=float)
    
    # Calculate the exponential of the adjacency matrix
    exp_A = np.exp(A)
    
    # Compute the substitution matrix, the inverse of which is the matrix of friction coefficients
    aux = np.linalg.pinv(np.eye(G.number_of_nodes()) - A)
    
    # Compute the communicability
    comm = np.multiply(exp_A, aux)
    
    return comm

# Example usage
if __name__ == "__main__":
    # Create an example graph
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 1), (4, 2), (4, 3)])
    
    # Compute communicability
    comm = communicability(G)
    
    print(comm)
