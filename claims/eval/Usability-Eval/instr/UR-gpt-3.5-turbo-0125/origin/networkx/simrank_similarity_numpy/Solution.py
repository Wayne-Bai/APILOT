
import numpy as np
import networkx as nx

def calculate_simrank(G, C=0.8, max_iter=100, eps=1e-4):
    nodes = list(G.nodes())
    num_nodes = len(nodes)
    sim_matrix = np.identity(num_nodes)  # Initialize similarity matrix with identity matrix
    
    # Create adjacency matrix
    A = nx.adjacency_matrix(G).toarray()
    
    for _ in range(max_iter):
        prev_sim_matrix = np.copy(sim_matrix)
        
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i == j:
                    continue
                
                neighbors_i = list(G.neighbors(nodes[i]))
                neighbors_j = list(G.neighbors(nodes[j]))
                
                if len(neighbors_i) == 0 or len(neighbors_j) == 0:
                    continue
                
                sim_ij = sum([prev_sim_matrix[nodes.index(u)][nodes.index(v)] for u in neighbors_i for v in neighbors_j]) / (len(neighbors_i) * len(neighbors_j))
                sim_matrix[i][j] = C / (len(neighbors_i) * len(neighbors_j)) * sim_ij
        
        if np.linalg.norm(sim_matrix - prev_sim_matrix) < eps:
            break
    
    return sim_matrix
