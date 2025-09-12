import networkx as nx

def quotient_graph(G, equivalence_relation):
    """
    Returns the quotient graph of G under the specified equivalence relation on nodes.

    Parameters:
    G (networkx.Graph): The input graph.
    equivalence_relation (function): A function that takes two nodes as input and returns True
                                      if the nodes are equivalent under the relation, otherwise False.

    Returns:
    networkx.Graph: The quotient graph.
    """
    
    # Create a mapping of the original nodes to their equivalence classes
    equivalence_classes = {}
    for node in G.nodes:
        found_class = False
        for class_repr in equivalence_classes:
            if equivalence_relation(node, class_repr):
                equivalence_classes[class_repr].append(node)
                found_class = True
                break
        if not found_class:
            equivalence_classes[node] = [node]
    
    # Create the quotient graph
    Q = nx.Graph()
    
    # Add nodes representing equivalence classes
    for class_repr in equivalence_classes:
        Q.add_node(class_repr)
    
    # Add edges between equivalence classes 
    for class_repr, nodes in equivalence_classes.items():
        for node in nodes:
            for neighbor in G.neighbors(node):
                neighbor_class = next((c for c, n in equivalence_classes.items() if neighbor in n), None)
                if neighbor_class and neighbor_class != class_repr:
                    Q.add_edge(class_repr, neighbor_class)
    
    return Q
