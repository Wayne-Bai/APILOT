import networkx as nx

def quotient_graph(G, equivalence_relation):
    # Create a dictionary to store the equivalence classes
    equivalence_classes = {equivalence_relation(node): set([node]) for node in G.nodes()}

    # Iterate over the nodes in the graph
    for node in G.nodes():
        # If the node is not in any equivalence class, create a new one
        if node not in equivalence_classes:
            equivalence_classes[equivalence_relation(node)] = set([node])
        # Otherwise, add the node to the existing equivalence class
        else:
            equivalence_classes[equivalence_relation(node)].add(node)

    # Create a new graph with the equivalence classes as nodes
    H = nx.Graph()

    # Iterate over the equivalence classes
    for equivalence_class in equivalence_classes.values():
        # Add a node to the new graph for each equivalence class
        H.add_node(equivalence_class)

        # Iterate over the edges in the original graph
        for u, v in G.edges():
            # If the endpoints of the edge are in the same equivalence class, add an edge to the new graph
            if equivalence_relation(u) == equivalence_relation(v):
                H.add_edge(equivalence_classes[equivalence_relation(u)], equivalence_classes[equivalence_relation(v)])

    return H
