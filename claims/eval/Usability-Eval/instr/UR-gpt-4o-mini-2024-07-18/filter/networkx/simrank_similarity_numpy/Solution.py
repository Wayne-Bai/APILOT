import numpy as np
import networkx as nx

def simrank(G, c=0.8, max_iter=100, tol=1e-5):
    nodes = list(G.nodes())
    n = len(nodes)
    sim = np.zeros((n, n))

    # Initialize similarity matrix for direct neighbors
    for i, u in enumerate(nodes):
        neighbors_u = set(G.neighbors(u))
        for j, v in enumerate(nodes):
            if i != j:
                neighbors_v = set(G.neighbors(v))
                sim[i, j] = len(neighbors_u.intersection(neighbors_v)) / (len(neighbors_u) * len(neighbors_v)) if neighbors_u and neighbors_v else 0

    # Iteratively update similarity matrix
    for iteration in range(max_iter):
        sim_old = sim.copy()
        for i, u in enumerate(nodes):
            for j, v in enumerate(nodes):
                if i != j:
                    sum_sim = 0.0
                    for neighbor_u in G.neighbors(u):
                        for neighbor_v in G.neighbors(v):
                            index_neighbor_u = nodes.index(neighbor_u)
                            index_neighbor_v = nodes.index(neighbor_v)
                            sum_sim += sim_old[index_neighbor_u, index_neighbor_v]
                    sim[i, j] = (c * sum_sim) / (len(list(G.neighbors(u))) * len(list(G.neighbors(v)))) if len(list(G.neighbors(u))) and len(list(G.neighbors(v))) else 0
        
        # Check for convergence
        if np.max(np.abs(sim - sim_old)) < tol:
            break

    return sim

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

sim_matrix = simrank(G)
print(sim_matrix)
