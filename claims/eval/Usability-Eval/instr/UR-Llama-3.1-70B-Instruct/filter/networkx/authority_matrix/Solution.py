import networkx as nx
import numpy as np

def hits_authority(G, max_iter=100, tol=1.0e-8, normalized=True):
    if not G:
        return {}

    # Normalize the adjacency matrix
    A = nx.to_numpy_array(G)
    degrees = A.sum(axis=0)
    degrees[degrees == 0] = 1
    A = A / degrees

    # Randomly initialize the hubs and authorities
    hubs = np.random.rand(len(G.nodes))
    authorities = np.random.rand(len(G.nodes))
    authorities /= authorities.sum()

    for _ in range(max_iter):
        last_auth = authorities
        authorities = np.dot(A.T, hubs)
        last_hubs = hubs
        hubs = np.dot(A, authorities)
        hubs /= hubs.sum()

        # Normalize authorities
        authorities /= authorities.sum()

        if np.linalg.norm(authorities - last_auth) < tol and np.linalg.norm(hubs - last_hubs) < tol:
            break

    # Return authorities only if normalized is True
    if normalized:
        return authorities
    else:
        return authorities, hubs

# Create a directed graph
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 1), (2, 1), (1, 3)])

# Get the HITS authority scores
authorities = hits_authority(G)
for i, auth in enumerate(authorities):
    print(f'Authority score for node {i+1} is: {auth}')
