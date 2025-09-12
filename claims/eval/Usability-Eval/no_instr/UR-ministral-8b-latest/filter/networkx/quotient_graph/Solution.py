import networkx as nx

def quotient_graph(G, node_equiv):
    # Create a quotient graph, representing the equivalence classes
    quotient_G = nx.Graph()

    # Create a dictionary to map nodes to their equivalence classes
    node_class = {}

    for node in G.nodes():
        if node not in node_class:
            # Create a new equivalence class and add node to it
            node_class[node] = [node]
        else:
            # Add node to its equivalence class
            node_class[node].append(node)

    # Create nodes in the quotient graph for each equivalence class
    for key, equivalence_class in node_class.items():
        quotient_G.add_node(equivalence_class)

    # Map edges to their corresponding equivalence classes
    for edge in G.edges():
        for node in edge:
            if node not in node_class:
                node_class[node] = [node]
        source = node_class[edge[0]]
        target = node_class[edge[1]]

        if source != target:
            quotient_G.add_edge(source, target)

    return quotient_G
