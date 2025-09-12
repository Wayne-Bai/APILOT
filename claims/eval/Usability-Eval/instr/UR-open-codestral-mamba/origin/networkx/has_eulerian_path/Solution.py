import networkx as nx

def has_eulerian_path(G, source=None):
    # Check if the graph is empty
    if G.number_of_edges() == 0:
        return False

    # If source is not specified, try to find all possible starting nodes
    if source is None:
        # A graph has an Eulerian path if it has at most two nodes with odd degree
        odd_degree_nodes = [node for node, degree in G.degree() if degree % 2 == 1]
        if len(odd_degree_nodes) > 2:
            return False
        elif len(odd_degree_nodes) == 2:
            # Try both nodes as the starting point
            node1, node2 = odd_degree_nodes
            return nx.has_eulerian_path(G.copy(), source=node1) or nx.has_eulerian_path(G.copy(), source=node2)

        # If all nodes have even degree, the graph has an Eulerian path or circuit
        return nx.is_connected(G)

    # Check if source is in the graph
    if source not in G:
        raise nx.NetworkXError(f"The graph {G} does not contain the node {source}.")

    # Check if the graph has an Eulerian path or circuit starting at the source
    try:
        nx.standard_basis(G.copy(), source=source, oriented=False)
        return True
    except nx.NetworkXNoCycle:
        return False
        