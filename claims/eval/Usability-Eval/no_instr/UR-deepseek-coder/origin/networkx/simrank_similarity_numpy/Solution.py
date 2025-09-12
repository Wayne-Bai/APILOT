import networkx as nx
import numpy as np

def simrank(G, c=0.8, max_iter=100, tol=1e-4):
    # Initialize SimRank matrix
    nodes = list(G.nodes())
    n = len(nodes)
    S = np.eye(n)
    
    # Create adjacency matrix
    A = nx.to_numpy_array(G, nodelist=nodes)
    
    # Normalize adjacency matrix
    A_norm = A / A.sum(axis=0)
    
    # Iterate to compute SimRank
    for _ in range(max_iter):
        prev_S = np.copy(S)
        S = np.eye(n)
        for i in range(n):
            for j in range(n):
                if i != j:
                    S[i, j] = c * np.sum(A_norm[:, i] * A_norm[:, j] * prev_S)
        
        # Check for convergence
        if np.linalg.norm(S - prev_S) < tol:
            break
    
    # Convert SimRank matrix to a dictionary
    simrank_dict = {nodes[i]: {nodes[j]: S[i, j] for j in range(n)} for i in range(n)}
    
    return simrank_dict

# Example usage
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
simrank_scores = simrank(G)
print(simrank_scores)
