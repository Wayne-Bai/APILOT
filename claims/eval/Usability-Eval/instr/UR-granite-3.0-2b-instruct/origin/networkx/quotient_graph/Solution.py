import networkx as nx

def quotient_graph(G, equivalence_relations):
    # Create a copy of the graph
    H = G.copy()

    # Define a function to map nodes to their equivalence class
    def map_nodes(node):
        for relation in equivalence_relations:
            if relation(node):
                return relation(node)
        return None

    # Map nodes to their equivalence classes
    H.nodes = {map_nodes(node): node for node in H.nodes}

    # Create a new graph with the mapped nodes
    H = nx.Graph(H)

    # Add edges between nodes in the same equivalence class
    for node in H.nodes:
        for neighbor in H.neighbors(node):
            if map_nodes(node) == map_nodes(neighbor):
                H.add_edge(node, neighbor)

    return H
