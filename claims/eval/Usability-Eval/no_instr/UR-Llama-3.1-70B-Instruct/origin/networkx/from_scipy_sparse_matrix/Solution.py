import networkx as nx
import numpy as np
from scipy import sparse

def sparse_matrix_to_nx_graph(adj_matrix):
    """
    Convert a scipy sparse matrix adjacency list to a networkx graph.

    Parameters:
    adj_matrix (scipy sparse matrix): Adjacency list in scipy sparse matrix format.

    Returns:
    graph (networkx graph): Networkx graph generated from the adjacency list.
    """
    graph = nx.Graph()
    
    # Get the number of nodes from the shape of the adjacency matrix
    num_nodes = adj_matrix.shape[0]
    
    # Add nodes to the graph
    graph.add_nodes_from(range(num_nodes))
    
    # Add edges to the graph
    graph.add_edges_from(zip(*adj_matrix.nonzero()))

    return graph

# Example usage:
if __name__ == "__main__":
    # Create a sample adjacency matrix
    adj_matrix = sparse.csr_matrix(np.array([
        [0, 1, 0, 0],
        [1, 0, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 0, 0]
    ]))

    # Convert the sparse matrix to a networkx graph
    graph = sparse_matrix_to_nx_graph(adj_matrix)

    # Print the graph
    print("Nodes:", list(graph.nodes()))
    print("Edges:", list(graph.edges()))
