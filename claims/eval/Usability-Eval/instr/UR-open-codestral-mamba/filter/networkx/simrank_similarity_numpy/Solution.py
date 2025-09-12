import numpy as np
import networkx as nx

G = nx.Graph()

def calculate_simrank(G):
    # Create matrices with the adjacency matrix and degree matrix components of the graph
    A = nx.to_numpy_array(G)
    D = np.diag(A.sum(axis=1))

    # Compute the inverse of the degree matrix
    D_inv = np.linalg.inv(D)

    # Compute the SimRank matrix
    S = np.dot(A, np.dot(D_inv, np.dot(D, A.T)))

    # Normalize SimRank scores
    S = S / np.max(S)

    # Compute SimRank of each node
    simrank_scores = S.sum(axis=1)
    simrank_scores = simrank_scores / np.max(simrank_scores)

    return simrank_scores

# Create a simple graph
G.add_edge("Alice", "Bob")
G.add_edge("Bob", "Charlie")
G.add_edge("Charlie", "Dave")
G.add_edge("Dave", "Eve")
G.add_edge("Eve", "Alice")

calculate_simrank(G)
