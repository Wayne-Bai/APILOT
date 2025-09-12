
from networkx import Graph

def get_quotient_graph(G, equivalent_nodes):
    """
    Returns the quotient graph of G under the specified equivalence relation on nodes.

    Parameters:
    G (networkx.Graph): The graph G.
    equivalent_nodes (dict): A dictionary where keys are nodes in G and values are their representative nodes under the equivalence relation.

    Returns:
    networkx.Graph: The quotient graph of G under the specified equivalence relation on nodes.
    """
    # Create a new empty graph
    H = Graph()

    # Add edges to the new graph based on the given equivalence relation
    for u, v in G.edges():
        if equivalent_nodes[u] == equivalent_nodes[v]:
            H.add_edge(equivalent_nodes[u], equivalent_nodes[v])

    # Return the quotient graph
    return H
