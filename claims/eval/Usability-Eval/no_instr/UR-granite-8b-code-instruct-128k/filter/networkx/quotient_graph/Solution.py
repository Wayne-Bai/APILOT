import networkx as nx
def quotient_graph(G, relation):
    # Create a new graph to hold the quotient graph
    quotient = nx.Graph()
    
    # Add nodes to the quotient graph based on the equivalence relation
    for node in G.nodes():
        equivalence_class = relation(node)
        quotient.add_node(equivalence_class)
    
    # Add edges to the quotient graph based on the equivalence relation
    for u, v in G.edges():
        equivalence_class_u = relation(u)
        equivalence_class_v = relation(v)
        if equivalence_class_u != equivalence_class_v:
            quotient.add_edge(equivalence_class_u, equivalence_class_v)
    
    return quotient
