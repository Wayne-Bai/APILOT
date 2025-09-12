import networkx as nx

def quotient_graph(G, equivalence_relation):
    # Create a new graph to store the quotient
    Q = nx.Graph()

    # Add nodes to the quotient graph
    for node in G.nodes():
        # Check if the node has any equivalent nodes
        if any(equivalence_relation(node, equiv_node) for equiv_node in G.nodes()):
            # Add the node to the quotient graph
            Q.add_node(node)

    # Add edges to the quotient graph
    for u, v in G.edges():
        # Check if the nodes are equivalent
        if any(equivalence_relation(u, equiv_node) and equivalence_relation(v, equiv_node) for equiv_node in G.nodes()):
            # Add the edge to the quotient graph
            Q.add_edge(u, v)

    return Q
