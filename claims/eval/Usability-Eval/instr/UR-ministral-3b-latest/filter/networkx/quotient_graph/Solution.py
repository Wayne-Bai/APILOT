import networkx as nx

def quotient_graph(G, R):
    """
    Returns the quotient graph G^R under the given equivalence relation R on nodes.

    Parameters:
    G (networkx.Graph): The input graph.
    R (networkx.Graph): The equivalence relation on nodes of G, needs to be a bijection.

    Returns:
    nx.Graph: The quotient graph G^R.
    """
    quotient = nx.Graph()

    # Add partitions of nodes to the quotient graph
    for V in R.nodes():
        quotient.add_node(V)

    # Add edges between partitions
    for V1, V2 in iter(R.edges()):
        quotient.add_edge(V1, V2)

    return quotient

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (3, 4)])
R = nx.Graph([(1, 3), (2, 4)])
quotient_G = quotient_graph(G, R)
print(quotient_G.edges())
