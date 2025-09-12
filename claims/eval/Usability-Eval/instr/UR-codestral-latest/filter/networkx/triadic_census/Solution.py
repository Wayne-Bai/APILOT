import networkx as nx

def triadic_census(G, nodelist=None):
    if nodelist is None:
        nodelist = G.nodes()

    # Initialize a dictionary to hold triad counts
    triad_counts = {triad_type: 0 for triad_type in range(16)}

    # Loop over all triplets of nodes
    for i in range(len(nodelist)):
        for j in range(i+1, len(nodelist)):
            for k in range(j+1, len(nodelist)):
                # Get the nodes
                node1, node2, node3 = nodelist[i], nodelist[j], nodelist[k]

                # Get the edges between the nodes
                edges = [(node1, node2) in G.edges(),
                         (node2, node1) in G.edges(),
                         (node1, node3) in G.edges(),
                         (node3, node1) in G.edges(),
                         (node2, node3) in G.edges(),
                         (node3, node2) in G.edges()]

                # Map the edges to a triad type
                triad_type = 0
                for idx, edge in enumerate(edges):
                    if edge:
                        triad_type += 2 ** idx

                # Update the count for this triad type
                triad_counts[triad_type] += 1

    return triad_counts
