
import networkx as nx

def min_weight_maximal_matching(G):
    pos = nx.max_weight_matching(G, maxcardinality=False)
    return pos

# Example usage
G = nx.complete_graph(5)
for (u, v) in G.edges():
    G[u][v]['weight'] = 1

mwm = min_weight_maximal_matching(G)
print(mwm)
