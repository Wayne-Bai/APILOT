import networkx as nx
import numpy as np

def simrank(G, r=0.8, max_iter=100, tol=1e-4):
    nodes = list(G.nodes())
    nodes_i = {nodes[i]: i for i in range(len(nodes))}
    
    # Initialize similarity matrix
    S = np.eye(len(nodes))
    
    for iter_step in range(max_iter):
        new_S = np.zeros_like(S)
        
        for u in nodes:
            for v in nodes:
                if u == v:
                    new_S[nodes_i[u], nodes_i[v]] = 1
                else:
                    # Get predecessors of u and v
                    predecessors_u = list(G.predecessors(u))
                    predecessors_v = list(G.predecessors(v))
                    
                    if predecessors_u and predecessors_v:
                        S_uv = sum(S[nodes_i[w], nodes_i[x]] for w in predecessors_u for x in predecessors_v)
                        new_S[nodes_i[u], nodes_i[v]] = r * S_uv / (len(predecessors_u) * len(predecessors_v))
        
        # Check for convergence
        if np.allclose(S, new_S, atol=tol):
            break
        S = new_S
    
    return S

# Example usage:
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 2), (1, 4), (4, 5)])

similarity_matrix = simrank(G)
print(similarity_matrix)
