import networkx as nx

def triadic_census(G, nodelist=None):
    """
    Compute the triadic census of a directed graph.

    Parameters:
    G (networkx.DiGraph): The directed graph.
    nodelist (list): List of nodes to consider. If None, all nodes are considered.

    Returns:
    dict: A dictionary where keys are triad types and values are counts.
    """
    triad_names = [
        "003", "012", "102", "021D", "021U", "021C", "111D", "111U",
        "030T", "030C", "201", "120D", "120U", "120C", "210", "300"
    ]
    triad_counts = {name: 0 for name in triad_names}

    if nodelist is None:
        nodelist = G.nodes()

    for node in nodelist:
        neighbors = set(G.predecessors(node)) | set(G.successors(node))
        for u in neighbors:
            if u == node:
                continue
            for v in neighbors:
                if v == node or v == u:
                    continue
                if not G.has_edge(u, v) and not G.has_edge(v, u):
                    triad_counts["003"] += 1
                elif G.has_edge(u, v) and G.has_edge(v, u):
                    triad_counts["102"] += 1
                elif G.has_edge(u, v) and not G.has_edge(v, u):
                    triad_counts["021D"] += 1
                elif not G.has_edge(u, v) and G.has_edge(v, u):
                    triad_counts["021U"] += 1
                elif G.has_edge(node, u) and G.has_edge(u, v) and G.has_edge(v, node):
                    triad_counts["120C"] += 1
                elif G.has_edge(node, u) and G.has_edge(u, v) and G.has_edge(node, v):
                    triad_counts["120U"] += 1
                elif G.has_edge(u, node) and G.has_edge(node, v) and G.has_edge(v, u):
                    triad_counts["120D"] += 1
                elif G.has_edge(u, node) and G.has_edge(node, v) and G.has_edge(u, v):
                    triad_counts["210"] += 1
                elif G.has_edge(u, node) and G.has_edge(v, node) and G.has_edge(u, v):
                    triad_counts["030T"] += 1
                elif G.has_edge(u, node) and G.has_edge(v, node) and G.has_edge(v, u):
                    triad_counts["030C"] += 1
                elif G.has_edge(node, u) and G.has_edge(node, v) and G.has_edge(u, v):
                    triad_counts["201"] += 1
                elif G.has_edge(node, u) and G.has_edge(node, v) and G.has_edge(v, u):
                    triad_counts["111U"] += 1
                elif G.has_edge(u, node) and G.has_edge(v, node) and G.has_edge(node, u):
                    triad_counts["111D"] += 1
                elif G.has_edge(u, node) and G.has_edge(v, node) and G.has_edge(node, v):
                    triad_counts["021C"] += 1
                elif G.has_edge(node, u) and G.has_edge(node, v) and G.has_edge(u, v) and G.has_edge(v, u):
                    triad_counts["300"] += 1

    return triad_counts

# Example usage:
# G = nx.DiGraph()
# G.add_edges_from([(1, 2), (2, 3), (3, 1)])
# census = triadic_census(G)
# print(census)
