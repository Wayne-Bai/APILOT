import networkx as nx

def triadic_census(G, nodelist=None):
    """
    Determines the triadic census of a directed graph.

    Parameters:
    G (networkx.DiGraph): The directed graph.
    nodelist (list): List of nodes to consider. If None, all nodes are considered.

    Returns:
    dict: A dictionary where keys are triad types and values are their counts.
    """
    triad_names = ["003", "012", "102", "021D", "021U", "021C", "111D", "111U", "030T", "030C", "201", "120D", "120U", "120C", "210", "300"]
    triad_counts = {name: 0 for name in triad_names}

    if nodelist is None:
        nodelist = list(G.nodes())

    # Generate all possible triads
    triads = []
    for n in nodelist:
        neighbors = set(G.predecessors(n)).union(G.successors(n))
        for u in neighbors:
            for v in neighbors:
                if u != v and frozenset([n, u, v]) not in triads:
                    triads.append(frozenset([n, u, v]))

    # Analyze each triad
    for triad in triads:
        triad = list(triad)
        edges = [(u, v) for u in triad for v in triad if u != v and (u, v) in G.edges()]
        triad_type = determine_triad_type(edges)
        triad_counts[triad_type] += 1

    return triad_counts

def determine_triad_type(edges):
    """
    Determines the type of a triad based on its edges.

    Parameters:
    edges (list): List of edges in the triad.

    Returns:
    str: The type of the triad.
    """
    triad_names = ["003", "012", "102", "021D", "021U", "021C", "111D", "111U", "030T", "030C", "201", "120D", "120U", "120C", "210", "300"]
    edge_count = len(edges)

    if edge_count == 0:
        return "003"
    elif edge_count == 1:
        return "012"
    elif edge_count == 2:
        if all(edges[0][::-1] != edges[1] for e in edges):
            return "102"
        elif edges[0][0] == edges[1][1] and edges[0][1] == edges[1][0]:
            return "021D"
        elif edges[0][0] == edges[1][0] and edges[0][1] == edges[1][1]:
            return "021U"
        else:
            return "021C"
    elif edge_count == 3:
        if all(edges[0][::-1] != edges[1] and edges[0][::-1] != edges[2] and edges[1][::-1] != edges[2] for e in edges):
            return "111D"
        elif all(edges[0][::-1] == edges[1] or edges[0][::-1] == edges[2] or edges[1][::-1] == edges[2] for e in edges):
            return "111U"
        elif (edges[0][0] == edges[1][1] and edges[0][1] == edges[1][0]) or (edges[0][0] == edges[2][1] and edges[0][1] == edges[2][0]) or (edges[1][0] == edges[2][1] and edges[1][1] == edges[2][0]):
            return "030T"
        else:
            return "030C"
    elif edge_count == 4:
        return "201"
    elif edge_count == 5:
        if all(edges[0][::-1] != edges[1] and edges[0][::-1] != edges[2] and edges[1][::-1] != edges[2] for e in edges):
            return "120D"
        elif all(edges[0][::-1] == edges[1] or edges[0][::-1] == edges[2] or edges[1][::-1] == edges[2] for e in edges):
            return "120U"
        else:
            return "120C"
    elif edge_count == 6:
        return "210"
    elif edge_count == 7:
        return "300"

# Example usage:
# G = nx.DiGraph()
# G.add_edges_from([(1, 2), (2, 3), (3, 1)])
# census = triadic_census(G)
# print(census)
