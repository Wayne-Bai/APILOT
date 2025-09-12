# Import necessary libraries
import networkx as nx
import numpy as np

def communicability(G):
    """
    Return subgraph communicability for all pairs of nodes in G.

    Parameters
    ----------
    G : NetworkX graph
        The input graph.

    Returns
    -------
    communicability : dictionary of dictionaries
        Dictionary of dictionaries where the first key is a node and the
        second key is a node and the value is the subgraph communicability
        between those two nodes.
    """
    # Get the adjacency matrix of the graph
    A = nx.to_numpy_array(G, dtype=int)

    # Calculate the matrix exponential of the adjacency matrix
    exp_A = np.exp(A)

    # Initialize an empty dictionary to store the results
    com = {}

    # Loop over all nodes in the graph
    for u in G.nodes():
        # Initialize an empty dictionary for node u
        com[u] = {}
        # Loop over all nodes in the graph
        for v in G.nodes():
            # Calculate the subgraph communicability between nodes u and v
            com[u][v] = exp_A[u, v] if u!= v else None

    return com

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4)])

# Calculate the subgraph communicability
com = communicability(G)

# Print the results
for u in com:
    for v in com[u]:
        if com[u][v] is not None:
            print(f"The subgraph communicability between nodes {u} and {v} is: {com[u][v]}")
