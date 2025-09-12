import networkx as nx
from collections import Counter

def triadic_census(G, nodelist=None):
    if nodelist is None:
        nodelist = G.nodes()

    # Create a subgraph from the nodelist
    H = G.subgraph(nodelist)

    # Get all triangles in the subgraph
    triangles = nx.triangles(H)

    # Create a list of all possible triad types
    triad_types = ['002', '011', '020', '101', '110', '120', '200',
                   '201', '210', '300']

    # Initialize a counter to store the counts of each triad type
    triad_counts = Counter()

    # Iterate over the triangles
    for n1, n2, n3 in triangles:
        # Get the degrees of the nodes in the triangle
        deg_n1 = G.degree(n1)
        deg_n2 = G.degree(n2)
        deg_n3 = G.degree(n3)

        # Construct the triad code
        triad_code = str(deg_n1) + str(deg_n2) + str(deg_n3)

        # Sort the triad code
        triad_code = ''.join(sorted(triad_code))

        # Increment the counter for the triad code
        triad_counts[triad_code] += 1

    # Return the counts of each triad type
    return [triad_counts[triad_type] for triad_type in triad_types]
