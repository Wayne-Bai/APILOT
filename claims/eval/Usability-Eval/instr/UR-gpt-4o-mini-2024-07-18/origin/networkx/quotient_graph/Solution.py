import networkx as nx

def quotient_graph(G, equivalence_classes):
    """
    Returns the quotient graph of G under the specified equivalence relation on nodes.

    Parameters:
    G : NetworkX graph
        The original graph.
    equivalence_classes : list of sets
        Each set contains nodes that are considered equivalent.

    Returns:
    Quotient Graph
    """
    # Create a new graph for the quotient
    Q = nx.Graph()

    # Map each equivalence class to a single node in the quotient graph
    mapping = {}
    for i, eq_class in enumerate(equivalence_classes):
        new_node = f"Q{i}"  # Label for the new node
        mapping[new_node] = eq_class

        # Add the new node to the quotient graph
        Q.add_node(new_node)

    # Add edges to the quotient graph
    for eq_class in equivalence_classes:
        for node in eq_class:
            for neighbor in G.neighbors(node):
                # Find the equivalence class of the neighbor
                for eq_class_neigh in equivalence_classes:
                    if neighbor in eq_class_neigh and eq_class_neigh != eq_class:
                        # Add an edge between the equivalent nodes in the quotient graph
                        Q.add_edge(mapping[new_node], mapping[f"Q{equivalence_classes.index(eq_class_neigh)}"])

    return Q

# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (4, 5), (5, 6)])
equivalence_classes = [{1, 2}, {3}, {4, 5, 6}]
Q = quotient_graph(G, equivalence_classes)
