import networkx as nx
import numpy as np

def simrank(G, r=0.9, max_iter=100, tol=1e-4):
    nodes = list(G.nodes())
    nodes_idx = {nodes[i]: i for i in range(len(nodes))}
    
    S = np.identity(len(nodes))  # initialize the similarity to identity matrix
    for _ in range(max_iter):
        new_S = np.zeros_like(S)
        
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if i != j:
                    # Retrieve predecessors of each node
                    predecessors_i = list(G.predecessors(nodes[i]))
                    predecessors_j = list(G.predecessors(nodes[j]))
                    
                    # Calculate the similarity based on predecessors
                    if predecessors_i and predecessors_j:
                        sim_sum = sum(
                            S[nodes_idx[p_i]][nodes_idx[p_j]] 
                            for p_i in predecessors_i 
                            for p_j in predecessors_j
                        )
                        new_S[i][j] = (r * sim_sum) / (len(predecessors_i) * len(predecessors_j))
        
        # Check for convergence
        if np.allclose(S, new_S, atol=tol):
            break
        S = new_S

    return S

# Example usage:
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

similarity_matrix = simrank(G)
print(similarity_matrix)
