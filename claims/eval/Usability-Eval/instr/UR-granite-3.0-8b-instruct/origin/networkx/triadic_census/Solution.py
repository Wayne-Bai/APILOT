import networkx as nx

def triadic_census(G, nodelist=None):
    # Create a dictionary to store the triadic census
    triadic_census = {}

    # Get the nodes in the graph
    nodes = list(G.nodes())

    # If a nodelist is provided, filter the nodes
    if nodelist:
        nodes = [node for node in nodes if node in nodelist]

    # Iterate over all triads in the graph
    for node1, node2, node3 in nx.triads(G):
        # Get the type of the triad
        triad_type = str(tuple(sorted([node1, node2, node3])))

        # If the triad type is not in the dictionary, add it
        if triad_type not in triadic_census:
            triadic_census[triad_type] = 0

        # Increment the count of the triad type
        triadic_census[triad_type] += 1

    return triadic_census
