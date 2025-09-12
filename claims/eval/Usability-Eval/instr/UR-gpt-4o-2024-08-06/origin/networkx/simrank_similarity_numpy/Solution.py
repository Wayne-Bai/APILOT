import networkx as nx
import numpy as np

def calculate_simrank(G, C=0.8, max_iter=100, tolerance=1e-6):
    nodes = list(G.nodes())
    index_map = {nodes[i]: i for i in range(len(nodes))}
    n = len(nodes)
    
    # Initialize the SimRank matrix
    S = np.identity(n, dtype=np.float64)

    for it in range(max_iter):
        # Initialize the new SimRank matrix
        new_S = np.identity(n, dtype=np.float64)

        # Iterate over each pair of nodes
        for u in nodes:
            for v in nodes:
                if u != v:
                    # Get the predecessors (in-neighbors) of u and v
                    pred_u = list(G.predecessors(u))
                    pred_v = list(G.predecessors(v))
                    
                    # Calculate numerator part of SimRank formula
                    if len(pred_u) > 0 and len(pred_v) > 0:
                        sum_sim = 0.0
                        for pu in pred_u:
                            for pv in pred_v:
                                index_pu = index_map[pu]
                                index_pv = index_map[pv]
                                sum_sim += S[index_pu][index_pv]

                        # Update the SimRank value
                        new_S[index_map[u]][index_map[v]] = (C * sum_sim) / (len(pred_u) * len(pred_v))
        
        # Check for convergence
        if np.allclose(S, new_S, atol=tolerance):
            break

        S = new_S

    # Create a mapping of node pairs to their SimRank score
    simrank_result = { (u, v): S[index_map[u]][index_map[v]] for u in nodes for v in nodes }

    return simrank_result

# Example usage
G = nx.DiGraph()
G.add_edges_from([(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)])

simrank_result = calculate_simrank(G)
print(simrank_result)
