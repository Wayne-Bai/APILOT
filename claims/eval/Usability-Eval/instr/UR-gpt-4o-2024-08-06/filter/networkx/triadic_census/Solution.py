import networkx as nx
from collections import Counter

def triadic_census(G, nodelist=None):
    if not G.is_directed():
        raise nx.NetworkXError("Triadic census is only defined for directed graphs.")
    
    triad_to_type = {
        (0, 0, 0): '003',
        (0, 0, 1): '012',
        (0, 1, 0): '012',
        (0, 1, 1): '102',
        (1, 0, 0): '012',
        (1, 0, 1): '102',
        (1, 1, 0): '021D',
        (1, 1, 1): '111D',
        (0, 2, 0): '021U',
        (0, 2, 1): '111U',
        (1, 2, 0): '021C',
        (1, 2, 1): '120D',
        (2, 0, 0): '021U',
        (2, 0, 1): '120U',
        (2, 1, 0): '021C',
        (2, 1, 1): '120C',
        (2, 2, 0): '030T',
        (2, 2, 1): '201',
        (1, 1, 2): '030C',
        (1, 2, 2): '210',
        (2, 1, 2): '210',
        (2, 2, 2): '300'
    }
    
    census = Counter()
    nodes = G.nodes() if nodelist is None else nodelist

    for u in nodes:
        for v in G.successors(u):
            if u == v:  # Avoid self-loops
                continue
            for w in G.successors(v):
                if u == w or v == w:  # Avoid duplicates
                    continue
                adjacency = (
                    G.has_edge(u, v) + G.has_edge(v, u),
                    G.has_edge(v, w) + G.has_edge(w, v),
                    G.has_edge(w, u) + G.has_edge(u, w)
                )
                triad_name = triad_to_type.get(adjacency)
                if triad_name:
                    census[triad_name] += 1

    return dict(census)

# Example of using the function:
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])
result = triadic_census(G)
print(result)
