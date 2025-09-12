
import networkx as nx

def directed_triadic_census(G, nodelist=None):
    triad_count = {
        '003': 0, '012': 0, '102': 0, '021D': 0, '021U': 0, '021C': 0, '111D': 0,
        '111U': 0, '030T': 0, '030C': 0, '201': 0, '120D': 0, '120U': 0, '120C': 0,
        '210': 0, '300': 0
    }

    if nodelist:
        node_set = set(nodelist)
        triads = nx.triads.triads_directed(G, nodes=node_set)
    else:
        triads = nx.triads.triads_directed(G)

    for triad_type in triads.values():
        triad_count[triad_type] += 1
        
    return triad_count

# Example usage
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 3), (3, 2)])

census = directed_triadic_census(G)
print("Triadic Census of the Directed Graph:")
print(census)
