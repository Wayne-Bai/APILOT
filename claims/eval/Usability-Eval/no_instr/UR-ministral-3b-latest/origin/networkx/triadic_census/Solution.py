import networkx as nx

def triadic_census(G, nodelist=None):
    triads, triad_counts = set(), 0

    if nodelist:
        subgraph = G.subgraph(nodelist)
    else:
        subgraph = G

    for u in subgraph.nodes:
        adjacents = list(subgraph.adj[u].keys())
        for v in adjacents:
            if adjacents.count(v) < 2:
                continue
            neighbors = list(subgraph.neighbors(v))
            if neighbors:
                neighbors.remove(u)
                if len(neighbors) >= 2:
                    for w in neighbors:
                        triads.add((u, v, w))
                        triad_counts += 1

    if nodelist and not triads:
        return None

    triadic_types = {frozenset(t): type(t) for t in [(1, 2), (1, 3), (3, 1), (3, 2), (2, 1), (2, 3), (9, 1), (9, 2), (1, 7), (1, 6), (2, 4), (2, 5), (4, 3), (4, 5), (3, 9), (5, 3), (5, 9)]}
    triads_counter = {frozenset(t): 0 for t in triadic_types}
    for triad in triads:
        triadic_type = frozenset(triad)
        triads_counter[triadic_type] += 1

    return triads_counter

# Example usage
G = nx.DiGraph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2), (2, 3)])
print(triadic_census(G))
