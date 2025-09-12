import networkx as nx

def triadic_census(G, nodelist=None):
    """
    Determine the triadic census of a directed graph.

    Parameters:
    G (networkx.DiGraph): The directed graph.
    nodelist (list, optional): A list of nodes to consider. If provided, only triads containing elements from this list are counted.

    Returns:
    dict: A dictionary containing the count of each triad type.
    """
    triad_counts = {
        '003': 0, '012': 0, '102': 0, '021': 0, '111': 0, '200': 0,
        '030': 0, '121': 0, '130': 0, '211': 0, '300': 0, '112': 0,
        '201': 0, '310': 0, '220': 0, '103': 0, '013': 0
    }

    for node in G.nodes():
        if nodelist and node not in nodelist:
            continue
        neighbors = list(G.successors(node))
        for i, n1 in enumerate(neighbors):
            for j, n2 in enumerate(neighbors[i+1:]):
                if nodelist and n1 not in nodelist or nodelist and n2 not in nodelist:
                    continue
                triad = tuple(sorted([node, n1, n2]))
                triad_type = ''.join(map(str, sorted([G[node][n1]['weight'], G[node][n2]['weight'], G[n1][n2]['weight']])))
                triad_counts[triad_type] += 1

    return triad_counts
