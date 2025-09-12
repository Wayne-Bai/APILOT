
import networkx as nx

def triadic_census(G, nodelist=None):
    """
    Determines the triadic census of a directed graph.

    The triadic census is a count of how many of the 16 possible types of triads are present in a directed graph. If a list of nodes is passed, then only those triads are taken into account which have elements of nodelist in them.

    Parameters
    ----------
    G : networkx.DiGraph
        The directed graph to calculate the triadic census for.
    nodelist : list, optional
        A list of nodes to restrict the calculation to. If not provided, all nodes in the graph are used.

    Returns
    -------
    counts : dict
        A dictionary mapping each of the 16 possible types of triads to its count in the directed graph.
    """
    if nodelist is None:
        nodelist = list(G)

    # Initialize the counts dictionary with all triad types set to 0
    counts = {triad_type: 0 for triad_type in range(16)}

    # Iterate over all possible triads in the graph
    for u, v, w in nx.directed_triads(G, nodelist):
        # Get the type of the current triad
        triad_type = get_triad_type(u, v, w)

        # Increment the count for the current triad type
        counts[triad_type] += 1

    return counts
