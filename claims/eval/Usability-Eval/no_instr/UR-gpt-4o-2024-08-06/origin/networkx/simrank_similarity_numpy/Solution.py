import networkx as nx
import numpy as np

def compute_simrank(graph, decay_factor=0.8, max_iter=100, tol=1e-4):
    nodes = list(graph.nodes())
    n = len(nodes)
    sim = np.identity(n)
    node_index = {nodes[i]: i for i in range(n)}

    for iteration in range(max_iter):
        prev_sim = sim.copy()

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                preds_i = list(graph.predecessors(nodes[i]))
                preds_j = list(graph.predecessors(nodes[j]))

                if len(preds_i) == 0 or len(preds_j) == 0:
                    sim[i][j] = 0
                else:
                    sim_sum = 0
                    for u in preds_i:
                        for v in preds_j:
                            sim_sum += prev_sim[node_index[u]][node_index[v]]

                    sim[i][j] = (decay_factor / (len(preds_i) * len(preds_j))) * sim_sum

        if np.allclose(sim, prev_sim, atol=tol):
            break

    return sim

# Example usage:
G = nx.DiGraph()
G.add_edge('A', 'C')
G.add_edge('B', 'C')
G.add_edge('C', 'D')
G.add_edge('D', 'E')
G.add_edge('E', 'F')
G.add_edge('F', 'C')

simrank_matrix = compute_simrank(G)
print("SimRank similarity matrix:")
print(simrank_matrix)
